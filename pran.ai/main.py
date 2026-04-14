#!/usr/bin/env python3
"""
Main entry point for Pran.ai
"""

from src.agents.orchestrator import OrchestratorAgent
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Welcome to Pran.ai - Context-Aware Life Intelligence Ecosystem!")

    # Initialize the Orchestrator
    orchestrator = OrchestratorAgent()

    # Example high-stakes event
    event = "Career pivot: Decided to leave current job and start a new venture in AI."

    print(f"Processing event: {event}")
    response = orchestrator.process_event(event)
    print("Orchestrator Response:")
    print(response)

if __name__ == "__main__":
    main()