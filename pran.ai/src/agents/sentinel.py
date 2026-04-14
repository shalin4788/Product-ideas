from langchain_openai import ChatOpenAI
import os

class SentinelAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

    def manage(self, event: str) -> str:
        """Manage operational logistics and send proactive nudges."""
        prompt = f"""
        As the Sentinel, for this life event: {event}
        Suggest operational tasks, logistics to handle, and proactive nudges or reminders.
        Provide a management plan.
        """
        response = self.llm.invoke(prompt)
        return response.content