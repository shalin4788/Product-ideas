from langchain_openai import ChatOpenAI
import os

class MatchmakerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

    def scout(self, event: str) -> str:
        """Scout human capital like VCs or recruiters to accelerate outcomes."""
        prompt = f"""
        As the Matchmaker, based on this life event: {event}
        Identify relevant human capital such as VCs, recruiters, mentors, or partners that could help.
        Suggest potential connections and how to reach them.
        """
        response = self.llm.invoke(prompt)
        return response.content