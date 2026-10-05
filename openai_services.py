from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage


from guitars_repository import guitar_repository

load_dotenv()

@tool
def get_guitars(limit: int | None=None):
    """Retrieve guitars from the database.

    Use this tool when the user asks to:
    - see guitars
    - list guitars
    - browse guitars
    - show available guitars
    - see featured guitars
    - get guitars from the database

    Return the guitars retrieved from the database.
    
    """ 
    guitars=guitar_repository.get_guitars_list(limit=limit)
    return  guitars

@tool
def get_guitar_details(guitar_id:int):
    """Retrieve detailed information about one guitar.

    Use this tool when the user asks about a specific guitar
    and provides its guitar ID.

    Return the details of that guitar from the database.
    """
    guitar=guitar_repository.get_guitar_details(guitar_id=guitar_id)
    return guitar

tools=[
    get_guitars,
    get_guitar_details
]

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5

)

llmtools=llm.bind_tools(tools)

def Convo(message: str):
    messages = [HumanMessage(content=message)]
    response = llmtools.invoke(messages)

    tools = {
        "get_guitars": get_guitars,
        "get_guitar_details": get_guitar_details
        }

    if response.tool_calls:
        messages.append(response)

        for call in response.tool_calls:
            tool = tools[call["name"]]
            result = tool.invoke(call["args"])

            messages.append(
                ToolMessage(content=str(result), tool_call_id=call["id"]))

        response = llmtools.invoke(messages)
    return response


