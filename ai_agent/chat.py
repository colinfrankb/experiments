from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.config import RunnableConfig

load_dotenv()

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# Using a Prompt Template
#
# system_template = "Translate the following from English into {language}"
# prompt_template = ChatPromptTemplate.from_messages(
#     [("system", system_template), ("user", "{text}")]
# )
# prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})


# The LLM requires the full chat history, for maintain context
# https://python.langchain.com/docs/concepts/chat_history/
#
# response_message = model.invoke([
#     HumanMessage(content="Hi! I'm Colin"),
#     AIMessage(content="Hello Colin! How can I help you today?"),
#     HumanMessage(content="What is my name?")
# ])


# Using LangGraph to maintain Chat History

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)

# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory and initialize CompiledStateGraph
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config: RunnableConfig = {"configurable": {"thread_id": "abc123"}}

output = app.invoke({"messages": [HumanMessage(content="Hi! I'm Colin")]}, config)
output["messages"][-1].pretty_print()  # The last message in the state is the response from the LLM

output = app.invoke({"messages": [HumanMessage(content="What's my name")]}, config)
output["messages"][-1].pretty_print()
