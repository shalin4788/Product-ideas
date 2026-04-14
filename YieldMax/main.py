"""YieldMax - Main entry point"""

import os
from dotenv import load_dotenv
from src.core import Orchestrator


def main():
    """Main application entry point"""
    load_dotenv()

    # Initialize orchestrator
    orchestrator = Orchestrator()

    print("YieldMax - Autonomous High-Yield Portfolio Management")
    print("=" * 50)
    print("Orchestrator initialized with:")
    print("  - Scout Agent (Category monitoring)")
    print("  - Enforcer Agent (Credit tracking)")
    print("  - Auditor Agent (ROI analysis)")


if __name__ == "__main__":
    main()
