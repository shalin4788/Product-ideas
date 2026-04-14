from langchain_openai import ChatOpenAI
import os

class PlannerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

    def plan(self, event: str) -> str:
        """Generate multi-horizon goals and next best actions."""
        prompt = f"""
        As the Planner, analyze this life event: {event}
        Map out multi-horizon goals (short-term, medium-term, long-term) and suggest next best actions.
        Provide a structured plan.
        """
        response = self.llm.invoke(prompt)
        return response.content