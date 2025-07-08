
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from tools.blablacar import get_blabla_trips
from tools.aireuropa import get_air_europa_flights

tools = [
    Tool(
        name="get_blabla_trips",
        func=get_blabla_trips,
        description="Obtiene viajes de BlaBlaCar entre dos ciudades en una fecha concreta. Argumentos: from_city, to_city, date"
    ),
    Tool(
        name="get_air_europa_flights",
        func=get_air_europa_flights,
        description="Simula vuelos de Air Europa entre dos ciudades en una fecha concreta. Argumentos: from_city, to_city, date"
    )
]

llm = ChatOpenAI(temperature=0, model="gpt-4")
agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

def run_agent(query: str):
    return agent.run(query)
