import json
from typing import Annotated, Any
from typing_extensions import TypedDict

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.runnables.config import RunnableConfig
from langchain_core.tools import InjectedToolCallId, tool
from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.types import Command, interrupt


class BasicToolNode:
    def __init__(self, tools: list):
        self.tools_by_name = {tool.name: tool for tool in tools}

    def __call__(self, inputs: dict):
        if messages := inputs.get("messages", []):
            message = messages[-1]
        else:
            raise ValueError("No messages found in input")
        
        outputs = []
        for tool_call in message.tool_calls:
            tool_result = self.tools_by_name[tool_call["name"]].invoke(tool_call["args"])

            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"]
                )
            )

        return {"messages": outputs}


class State(TypedDict):
    messages: Annotated[list, add_messages]
    name: str
    birthday: str


def route_tools(state: State):
    """
    Use in the conditional_edge to route to the ToolNode if the last message
    has tool calls. Otherwise, route to the end. When adding the conditional edge
    it will always follow from the chatbot, which is why the message will always
    be an AIMessage
    """
    print("route_tools entered")

    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get("messages", []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")
    
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        print("has tool_calls")

        # the string value returned is the name of the next node
        return "tools"

    return END


@tool(description="Gets the lunch menu for a given restaurant")
def get_lunch_menu(restaurant: str) -> str:
    return f"For {restaurant} its Fish and Chips"


# I'm not sure how the human must actually interact in the flow here
@tool(description="Request assistance from human")
def human_assistance(
    name: str,
    birthday: str,
    tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    human_response = interrupt({
        "question": "Is this correct?",
        "name": name,
        "birthday": birthday,
    })

    # If the information is correct, update the state as-is.
    if human_response.get("correct", "").lower().startswith("y"):
        verified_name = name
        verified_birthday = birthday
        response = "Correct"
    # Otherwise, receive information from the human reviewer.
    else:
        verified_name = human_response.get("name", name)
        verified_birthday = human_response.get("birthday", birthday)
        response = f"Made a correction: {human_response}"

    # This time we explicitly update the state with a ToolMessage inside
    # the tool.
    state_update = {
        "name": verified_name,
        "birthday": verified_birthday,
        "messages": [ToolMessage(response, tool_call_id=tool_call_id)]
    }

    return Command(update=state_update)


def chatbot(state: State):
    message: Any = llm.invoke(state["messages"])
    # Because we will be interrupting during tool execution,
    # we disable parallel tool calling to avoid repeating any
    # tool invocations when we resume.
    assert len(message.tool_calls) <= 1
    return {"messages": [message]}


load_dotenv()

tools = [get_lunch_menu, human_assistance]

llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai").bind_tools(tools)

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=tools))

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)


def stream_graph_updates(user_input: str):
    config: RunnableConfig = {"configurable": {"thread_id": "1"}}
    for event in graph.stream({"messages": [HumanMessage(content=user_input)]}, config=config, stream_mode="values"):
        if "messages" in event:
            event["messages"][-1].pretty_print()


def stream_graph_updates_from_human_assistance() -> None:
    config: RunnableConfig = {"configurable": {"thread_id": "1"}}
    human_command: Command = Command(
        resume={
            "name": "Bailey",
            "birthday": "Nov 30, 2016",
        },
    )
    # human_command: Command = Command(resume={"data": "We recommend you get a new job"})
    for event in graph.stream(human_command, config=config, stream_mode="values"):
        if "messages" in event:
            event["messages"][-1].pretty_print()


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        if user_input.startswith("Human Assistance"):
            stream_graph_updates_from_human_assistance()
        else:
            stream_graph_updates(user_input)
    except:
        user_input = "What do you know about LangGraph?"
        print(f"User: {user_input}")
        stream_graph_updates(user_input)
        break
