from datetime import date

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langchain_core.runnables.config import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel


load_dotenv()


class WeatherResponse(BaseModel):
    conditions: str


@tool(description="Gets weather information given a city", parse_docstring=False)
def get_weather(city: str) -> str:
    return f"It's always rainy in {city}"


@tool(description="Gets the lunch menu for a given city", parse_docstring=False)
def get_lunch_menu(city: str) -> str:
    return f"Burgers and chips"


@tool(description="Create an item in a todo list", parse_docstring=False)
def create_todo_list_item(description: str, due_date: date):
    return f"{description}, due on {due_date}"


model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

checkpointer = InMemorySaver()

agent_executor = create_react_agent(
    model,
    tools=[get_weather, get_lunch_menu, create_todo_list_item],
    prompt="You are a helpful assistant",
    # checkpointer=checkpointer,
    response_format=WeatherResponse
)

config: RunnableConfig = {"configurable": {"thread_id": 1}}

response = agent_executor.invoke(
    {
        "messages": [
            HumanMessage(content="I want to create a todo list item"),
            AIMessage(content="What is the description and due date?"),
            HumanMessage(content="The description is to make breakfast"),
            AIMessage(content="What is the due date?"),
            HumanMessage(content="The due date is 2025-01-02"),
        ]
    },
    # config
)

# print(response)

for message in response["messages"]:
    message.pretty_print()

