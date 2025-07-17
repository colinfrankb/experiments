from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.runnables.config import RunnableConfig
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent


@tool(description="Gets the lunch menu for a given restaurant")
def get_lunch_menu(restaurant: str) -> str:
    return f"For {restaurant} its Fish and Chips"


load_dotenv()

llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

checkpointer = InMemorySaver()

agent = create_react_agent(
    llm,
    tools=[get_lunch_menu],
    checkpointer=checkpointer
)

def stream_graph_updates(user_input: str):
    config: RunnableConfig = {"configurable": {"thread_id": "1"}}
    for event in agent.stream({"messages": [HumanMessage(content=user_input)]}, config=config, stream_mode="values"):
        if "messages" in event:
            event["messages"][-1].pretty_print()

while True:
    user_input = input("User:")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    stream_graph_updates(user_input)
