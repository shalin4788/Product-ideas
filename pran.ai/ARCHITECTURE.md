# pran.ai - Technical Architecture & Tech Stack

**Context-Aware Life Intelligence Ecosystem**

---

## 🏛️ System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACE LAYER                     │
│         (Web Dashboard / Mobile App / API Clients)           │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│                   EVENT INGESTION LAYER                      │
│   (Life Events: Career Pivots, Job Loss, Founder Transition) │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│                                                               │
│                 🎯 ORCHESTRATOR (CORE)                       │
│          Event Detection & Agent Coordination Hub            │
│                                                               │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  • Intent Decomposition                                │  │
│  │  • Task Routing & Prioritization                       │  │
│  │  • Multi-Agent Coordination                            │  │
│  │  • Context Management & State Tracking                 │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                               │
└─────────────────┬───────────────────────────────────────────┘
                  │
      ┌───────────┴───────────┬────────────────┬─────────────┐
      │                       │                │             │
      ▼                       ▼                ▼             ▼
┌──────────────┐      ┌──────────────┐   ┌──────────────┐ ┌──────────────┐
│   PLANNER    │      │  MATCHMAKER  │   │   SENTINEL   │ │   AUDITOR    │
│   AGENT      │      │   AGENT      │   │   AGENT      │ │   AGENT      │
├──────────────┤      ├──────────────┤   ├──────────────┤ ├──────────────┤
│ • Goal Mapping│     │• Human Capital│   │• Operational │ │• Risk & Comp │
│ • Horizon     │     │  Scouting     │   │  Management  │ │  Validation  │
│  Planning     │     │• VC/Recruiter│   │• Proactive   │ │• Guardrails  │
│ • Action      │     │  Network     │   │  Nudges      │ │• Compliance  │
│  Sequencing   │     │  Building    │   │• Logistics   │ │  Check       │
│ • Milestones  │     │• Opportunity │   │• Notifications│ │              │
│  Tracking     │     │  Scoring     │   │  & Reminders  │ │              │
└──────────────┘      └──────────────┘   └──────────────┘ └──────────────┘
      │                       │                │             │
      └───────────┬───────────┴────────────────┴─────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│                  DATA & CONTEXT LAYER                        │
│                                                               │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Knowledge Base │ Goal State │ User Profile │ Decisions  │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                               │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│              EXTERNAL INTEGRATIONS LAYER                     │
│                                                               │
│  • LLM APIs (Claude, Gemini)  • CRM Systems                 │
│  • Calendar Systems (Google/Outlook)  • Email Platforms     │
│  • Networking APIs (LinkedIn)  • Productivity Tools          │
│  • Document Storage (Drive/OneDrive)  • Analytics Services   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### **Backend & Core Framework**
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.11+ | Primary development language |
| **Runtime** | Python Virtual Environment (venv/conda) | Isolated dependency management |
| **Orchestration** | Python-based Event Loop | Agent coordination & state management |
| **LLM Integration** | LangChain / LlamaIndex | Multi-model LLM orchestration |
| **Type Safety** | Pydantic | Data validation & schema management |

### **AI/ML Components**
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM Providers** | Claude (Anthropic), Gemini (Google) | Multi-model inference for reasoning & planning |
| **Embeddings** | OpenAI Embeddings / Sentence Transformers | Semantic search & context retrieval |
| **Vector Database** | Pinecone / Weaviate / Chromadb | Semantic memory & knowledge storage |
| **Reasoning Engine** | ReAct / Chain-of-Thought | Agent decision-making framework |
| **Function Calling** | Tool Use / Function Calling APIs | Structured agent actions |

### **Data Management**
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Primary Database** | PostgreSQL (or MongoDB) | Persistent state, user data, goals |
| **Cache Layer** | Redis | Session management, quick retrieval |
| **Message Queue** | Celery + Redis/RabbitMQ | Async task processing |
| **Data Validation** | Pydantic / JSONSchema | Schema enforcement across APIs |
| **ORM** | SQLAlchemy (Python) | Database abstraction layer |

### **API & Communication**
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | FastAPI / Flask | RESTful API & async endpoints |
| **Real-time** | WebSockets / Server-Sent Events (SSE) | Live notifications & status updates |
| **API Auth** | JWT / OAuth 2.0 | User authentication & authorization |
| **Rate Limiting** | Token bucket / Fixed window | API throttling & quota management |

### **Frontend (Optional)**
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | React.js / Vue.js | Interactive dashboard UI |
| **State Management** | Redux / Zustand | Client-side state management |
| **UI Library** | Tailwind CSS / Material UI | Component styling & theming |
| **Charting** | Recharts / Chart.js | Goal progress visualization |

### **DevOps & Infrastructure**
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Containerization** | Docker | Application containerization |
| **Orchestration** | Kubernetes / Docker Compose | Container orchestration |
| **CI/CD** | GitHub Actions / GitLab CI | Automated testing & deployment |
| **Monitoring** | Prometheus + Grafana / DataDog | System health & performance tracking |
| **Logging** | ELK Stack / Datadog | Centralized log aggregation |
| **Cloud Platform** | AWS / GCP / Azure | Hosting & managed services |

### **Development Tools**
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Testing** | pytest | Unit & integration testing |
| **Code Quality** | Black, Flake8, MyPy | Linting, formatting, type checking |
| **Documentation** | Sphinx / MkDocs | Auto-generated docs |
| **Version Control** | Git + GitHub | Source code management |
| **Environment Management** | python-dotenv | Configuration management |

---

## 🔄 Data Flow Diagram

```
User Input / External Event
        │
        ▼
┌──────────────────────────────────────┐
│  EVENT INGESTION & NORMALIZATION    │
│  • Parse life events                 │
│  • Extract entities & context        │
│  • Timestamp & categorize            │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  ORCHESTRATOR PROCESSING             │
│  • Decompose intent                  │
│  • Assess urgency & priority         │
│  • Route to specialized agents       │
└────────┬─────────────────────────────┘
         │
    ┌────┴────┬──────────┬──────────┐
    │          │          │          │
    ▼          ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌─────────┐
│Planner │ │Matcher │ │Sentinel│ │Auditor  │
└────┬───┘ └───┬────┘ └───┬────┘ └────┬────┘
     │         │          │           │
     └────┬────┴──────────┴───────────┘
          │
          ▼
┌──────────────────────────────────────┐
│  DECISION AGGREGATION                │
│  • Merge agent outputs               │
│  • Resolve conflicts                 │
│  • Prioritize actions                │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  PERSISTENCE & NOTIFICATIONS         │
│  • Store decisions & state           │
│  • Queue notifications               │
│  • Update user dashboard             │
└──────────────────────────────────────┘
```

---

## 🏗️ Core Modules & Responsibilities

### **Orchestrator Module** (`orchestrator.py`)
- **Responsibilities:**
  - Event reception & validation
  - Intent decomposition using LLM
  - Agent task distribution
  - State management & context window
  - Conflict resolution across agents
  - Response aggregation & prioritization

- **Key Methods:**
  ```python
  async process_event(event: LifeEvent) -> Decisions
  decompose_intent(event: LifeEvent) -> Tasks
  route_to_agents(tasks: Tasks) -> Dict[Agent, Task]
  aggregate_responses(responses: Dict) -> Decisions
  ```

---

### **Planner Agent** (`planner.py`)
- **Responsibilities:**
  - Multi-horizon goal decomposition (3-month, 1-year, 5-year)
  - Next best action sequencing
  - Milestone tracking & verification
  - Opportunity scoring
  - Long-term opportunity planning

- **Key Capabilities:**
  - Goal mapping frameworks (OKRs, SMART goals)
  - Dependency analysis
  - Timeline optimization
  - Risk-adjusted action sequencing

---

### **Matchmaker Agent** (`matchmaker.py`)
- **Responsibilities:**
  - Human capital identification
  - Network graph analysis
  - Opportunity-person matching
  - Introduction scoring & outreach sequencing
  - Relationship acceleration pathways

- **Key Capabilities:**
  - LinkedIn/network integration
  - Contextual relevance scoring
  - Warm introduction pathway mapping
  - Follow-up cadence optimization

---

### **Sentinel Agent** (`sentinel.py`)
- **Responsibilities:**
  - Daily workflow monitoring
  - Friction point detection
  - Operational nudges & reminders
  - Calendar optimization
  - Task prioritization in real-time

- **Key Capabilities:**
  - Contextual notification engine
  - Calendar conflict detection
  - Daily briefing generation
  - Just-in-time task suggestions

---

### **Auditor Agent** (Optional, from YieldMax Framework)
- **Responsibilities:**
  - Risk & compliance validation
  - Goal feasibility assessment
  - Timeline reasonableness checks
  - Guardrail enforcement

---

## 🔐 Security & Privacy

| Layer | Implementation |
|-------|-----------------|
| **Authentication** | JWT tokens with refresh rotation |
| **Authorization** | Role-based access control (RBAC) |
| **Encryption** | TLS 1.3 for transit, AES-256 at rest |
| **Data Privacy** | User data isolation, GDPR compliance |
| **Audit Logging** | Immutable transaction logs |
| **Secret Management** | Environment variables, HashiCorp Vault |

---

## 📊 Deployment Architecture

### **Development**
```
Local Machine
  ├── FastAPI Dev Server (localhost:8000)
  ├── SQLite / PostgreSQL (local)
  ├── Redis (local or Docker)
  └── LLM API keys (via .env)
```

### **Staging**
```
AWS / GCP / Azure
  ├── Docker container
  ├── Managed PostgreSQL
  ├── Managed Redis
  ├── API Gateway
  └── Load Balancer
```

### **Production**
```
Kubernetes Cluster
  ├── API Service (FastAPI pods)
  ├── Worker Service (Celery workers)
  ├── PostgreSQL (RDS / Cloud SQL)
  ├── Redis (ElastiCache / Memorystore)
  ├── Vector DB (Pinecone / Self-hosted)
  ├── Monitoring (Prometheus + Grafana)
  └── Logging (ELK Stack)
```

---

## 🚀 Scaling Considerations

### **Horizontal Scaling**
- **API Services:** Multiple FastAPI instances behind load balancer
- **Agent Processing:** Distributed Celery workers across machines
- **Vector Search:** Sharded Pinecone indexes by user segment

### **Vertical Scaling**
- **Database:** Read replicas for query scaling
- **Cache:** Redis cluster for distributed caching
- **Message Queue:** RabbitMQ for high-throughput event processing

### **Optimization Targets**
- Agent inference latency < 2s (p95)
- API response time < 500ms (p95)
- Event processing throughput > 1000 events/sec
- Database query time < 100ms (p95)

---

## 📋 Development Roadmap

### **Phase 1 (MVP)**
- [ ] Orchestrator core with single LLM
- [ ] Basic Planner agent (goal decomposition)
- [ ] REST API layer
- [ ] PostgreSQL + simple caching

### **Phase 2 (Enhancement)**
- [ ] Multi-agent coordination
- [ ] Vector DB for semantic memory
- [ ] Web dashboard
- [ ] Advanced authentication

### **Phase 3 (Scale)**
- [ ] Kubernetes deployment
- [ ] Advanced monitoring & alerting
- [ ] Mobile app integration
- [ ] Third-party integrations (LinkedIn, Calendar APIs)

### **Phase 4 (Production)**
- [ ] Full compliance & security audit
- [ ] Performance optimization
- [ ] Disaster recovery & backup strategy
- [ ] Enterprise features (teams, analytics)

---

## 🔗 External Integrations

| Service | Purpose | Authentication |
|---------|---------|-----------------|
| **Claude API** | Primary reasoning & planning | API Key |
| **Google Gemini** | Alternative model + multimodal | API Key |
| **Google Calendar** | Schedule optimization | OAuth 2.0 |
| **LinkedIn API** | Network intelligence | OAuth 2.0 |
| **Gmail API** | Email context | OAuth 2.0 |
| **Stripe** | Subscription management | API Key |
| **Slack** | Notifications & integration | Webhooks |

---

## 📝 API Endpoints (RESTful)

### **Events**
```
POST   /api/events              → Ingest life event
GET    /api/events/:id          → Get event details
GET    /api/events              → List recent events
DELETE /api/events/:id          → Archive event
```

### **Goals**
```
GET    /api/goals               → List user goals
POST   /api/goals               → Create goal
PUT    /api/goals/:id           → Update goal
GET    /api/goals/:id/progress  → Goal progress tracking
```

### **Actions**
```
GET    /api/actions             → List recommended actions
POST   /api/actions/:id/done    → Mark action complete
GET    /api/actions/suggested   → Get AI suggestions
```

### **Agents**
```
GET    /api/agents/status       → Agent health status
POST   /api/agents/:name/retry  → Retry agent task
```

---

## 🧪 Testing Strategy

| Type | Framework | Coverage Target |
|------|-----------|-----------------|
| **Unit Tests** | pytest | 80%+ |
| **Integration Tests** | pytest + fixtures | 60%+ |
| **Agent Tests** | Custom + mocked LLMs | 70%+ |
| **E2E Tests** | Selenium / Playwright | Key user flows |
| **Load Tests** | Locust | 1000 RPS |

---

## 📚 Dependencies (requirements.txt)

### **Core**
```
python>=3.11
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0
```

### **AI/ML**
```
anthropic>=0.7.0
google-generativeai>=0.3.0
langchain>=0.1.0
openai>=1.3.0
```

### **Data**
```
sqlalchemy>=2.0
psycopg2-binary>=2.9
redis>=5.0
```

### **Utils**
```
python-dotenv>=1.0
requests>=2.31.0
httpx>=0.25.0
aiohttp>=3.9.0
```

### **Development**
```
pytest>=7.4.0
black>=23.11.0
flake8>=6.1.0
mypy>=1.7.0
```

---

## 🎯 Success Metrics

| Metric | Target | Measurement |
|--------|--------|------------|
| **Agent Accuracy** | > 90% | Human evaluation of recommendations |
| **API Latency** | < 500ms p95 | Application monitoring |
| **System Uptime** | > 99.9% | Infrastructure monitoring |
| **User Engagement** | > 70% | Action completion rate |
| **Cost per User** | < $5/month | Infrastructure + LLM costs |

---

## 📖 References & Resources

- [LangChain Documentation](https://python.langchain.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Anthropic Claude API](https://docs.anthropic.com)
- [PostgreSQL Documentation](https://www.postgresql.org/docs)
- [Kubernetes Best Practices](https://kubernetes.io/docs)

---

**Last Updated:** April 2026  
**Maintainer:** Shalin Gosalia  
**Status:** Active Development
