# YieldMax - Autonomous High-Yield Portfolio Management

A proactive credit intelligence platform that eliminates "Value Leakage" through an Orchestrator that monitors real-time spend and lifestyle shifts to direct specialized agents.

## Product Overview

YieldMax is an intelligent credit card portfolio manager that optimizes rewards capture, tracks benefits, and audits card ROI to eliminate wasted value.

### Core Agents

- **The Scout**: Monitors spending categories to recommend the next best card for reward capture
- **The Enforcer**: Tracks itemized credits and fires nudges to ensure no benefit expires
- **The Auditor**: Quantifies realized ROI vs fees to deliver "Keep or Cancel" verdicts

### Key Features

- Real-time spend monitoring and analysis
- Proactive credit card recommendations
- Automated benefit tracking and expiration alerts
- ROI analysis and card optimization verdicts

## Project Structure

```
YieldMax/
├── src/
│   ├── agents/          # Scout, Enforcer, Auditor agents
│   ├── core/            # Orchestrator and core logic
│   └── utils/           # Shared utilities and helpers
├── config/              # Configuration files
├── docs/                # Documentation
├── tests/               # Test suite
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Configure environment: `cp .env.example .env`
3. Run the application: `python main.py`

## Development

- Add agent implementations in `src/agents/`
- Core orchestrator logic in `src/core/`
- Tests in `tests/`
