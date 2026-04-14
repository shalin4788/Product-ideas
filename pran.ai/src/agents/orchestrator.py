from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool
from .planner import PlannerAgent
from .matchmaker import MatchmakerAgent
from .sentinel import SentinelAgent
import os

class OrchestratorAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.planner = PlannerAgent()
        self.matchmaker = MatchmakerAgent()
        self.sentinel = SentinelAgent()

        # Define tools for the orchestrator
        @tool
        def plan_goals(event: str) -> str:
            """Plan multi-horizon goals and next best actions based on the event."""
            return self.planner.plan(event)

        @tool
        def scout_network(event: str) -> str:
            """Scout human capital like VCs or recruiters."""
            return self.matchmaker.scout(event)

        @tool
        def manage_operations(event: str) -> str:
            """Manage operational logistics and send proactive nudges."""
            return self.sentinel.manage(event)

        tools = [plan_goals, scout_network, manage_operations]

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are the Orchestrator for a Context-Aware Life Intelligence Ecosystem. "
                       "When a high-stakes life event occurs, coordinate responses from Planner, Matchmaker, and Sentinel. "
                       "Analyze the event and decide which agents to activate."),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])

        agent = create_openai_functions_agent(self.llm, tools, prompt)
        self.executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def process_event(self, event: str) -> str:
        """Process a life event and coordinate responses."""
        response = self.executor.invoke({"input": f"High-stakes event: {event}. Coordinate the appropriate responses."})
        return response["output"]