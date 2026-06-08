# Investigation Orchestrator

Coordinating Intelligence, Agents and Investigation Workflows Across the Financial Crime Intelligence Platform

---

# Executive Summary

The Investigation Orchestrator is the central coordination capability within the AI Investigator Copilot architecture.

While specialist agents provide domain expertise and the Case Intelligence Agent provides investigation context, the Investigation Orchestrator determines how intelligence should be assembled, which agents should contribute and how investigator questions should be answered.

The Investigation Orchestrator does not perform specialist analysis.

The Investigation Orchestrator determines which specialist capabilities should be engaged.

It acts as the coordination layer that transforms a collection of individual agents into a unified intelligence platform.

---

# Purpose

The purpose of the Investigation Orchestrator is to:

- Interpret investigator requests
- Select appropriate specialist agents
- Coordinate intelligence gathering
- Manage investigation workflows
- Assemble investigation context
- Synthesize intelligence outputs
- Support investigator decision making

The Investigation Orchestrator becomes the operational brain of the AI Investigator Copilot architecture.

---

# Position Within The Architecture

```text
Investigator
        ↓

Conversational Copilot
        ↓

Investigation Orchestrator
        ↓

Network Agent
TBML Agent
Correspondent Banking Agent
Capital Markets Agent
Sanctions Agent
Threat Intelligence Agent
Case Intelligence Agent

        ↓

Response Synthesis

        ↓

Investigator Response
```

The Orchestrator sits between investigator requests and specialist intelligence capabilities.

---

# Core Principle

Specialist agents provide intelligence.

The Investigation Orchestrator coordinates intelligence.

```text
Question
        ↓
Orchestrator
        ↓
Specialist Agents
        ↓
Response
```

Without the Orchestrator:

```text
Multiple Independent Agents
```

With the Orchestrator:

```text
Coordinated Intelligence Platform
```

---

# Question Interpretation

The first responsibility of the Orchestrator is understanding investigator intent.

Example:

```text
Why is this customer high risk?
```

The Orchestrator determines:

```text
Required Intelligence

- Risk scoring
- Network relationships
- Sanctions exposure
- Case context
```

It then activates the appropriate agents.

---

# Agent Selection

Different questions require different intelligence sources.

Example:

```text
Explain this trade transaction.
```

Selected Agents:

```text
TBML Agent

Case Intelligence Agent
```

---

Example:

```text
Summarise this investigation.
```

Selected Agents:

```text
Case Intelligence Agent

Threat Intelligence Agent

Network Agent
```

---

Example:

```text
Explain this payment route.
```

Selected Agents:

```text
Correspondent Banking Agent

Network Agent

Case Intelligence Agent
```

The Orchestrator ensures only relevant agents participate.

---

# Workflow Coordination

The Orchestrator manages intelligence gathering workflows.

```text
Investigator Question
          ↓
Intent Analysis
          ↓
Agent Selection
          ↓
Intelligence Collection
          ↓
Response Assembly
          ↓
Investigator Response
```

This creates a structured reasoning process.

---

# Threat Intelligence Integration

The Orchestrator determines when external intelligence should contribute.

Example:

```text
Why is this vessel high risk?
```

The Orchestrator may activate:

```text
Sanctions Agent

Threat Intelligence Agent

Case Intelligence Agent
```

This allows emerging threat intelligence to be incorporated when relevant.

# Case Intelligence Integration

The Case Intelligence Agent plays a central role in orchestration.

Specialist agents provide findings.

The Case Intelligence Agent provides investigation context.

```text
Specialist Findings
        ↓
Case Intelligence Agent
        ↓
Investigation Context
        ↓
Orchestrator
```

The Orchestrator uses this context to build coherent responses.

---

# Response Synthesis

The Orchestrator assembles intelligence from multiple sources.

Example:

```text
TBML Agent

Invoice inflation identified
```

```text
Network Agent

Shared ownership identified
```

```text
Sanctions Agent

Indirect exposure identified
```

```text
Threat Intelligence Agent

Behaviour consistent with emerging
sanctions evasion typology
```

The Orchestrator combines these findings into a unified response.

---

# Multi-Agent Collaboration

Future architectures may support simultaneous collaboration between multiple agents.

```text
Investigator Question
          ↓

Investigation Orchestrator

          ↓

Network Agent

TBML Agent

Correspondent Banking Agent

Capital Markets Agent

Sanctions Agent

Threat Intelligence Agent

Case Intelligence Agent

          ↓

Intelligence Synthesis

          ↓

Response Generation
```

The Orchestrator ensures all relevant intelligence is incorporated.

---

# Investigation Support Flow Integration

The Orchestrator may support:

- Alert Rationales
- Investigator Summaries
- Evidence Packs
- Intelligence Reports
- Case Packages
- Conversational Copilot Responses

The capability acts as the coordination layer across all investigation workflows.

---

# Governance Considerations

The Investigation Orchestrator must:

- Maintain traceability
- Record agent participation
- Support auditability
- Preserve evidence references
- Prevent unsupported conclusions
- Support human review

All orchestration decisions should be explainable and auditable.

---

# Future Agentic Architecture

Future enhancements may include:

- Dynamic workflow planning
- Autonomous evidence retrieval
- Agent confidence scoring
- Investigation planning agents
- Typology recommendation agents
- Automated task delegation
- Continuous intelligence monitoring

These capabilities will support increasingly sophisticated intelligence-led investigations.

---

# Navigation

- [AI Investigator Copilot](../README.md)
- [Reference Architecture](../reference-architecture/README.md)
- [Governance](../governance/README.md)
- [Evaluation Framework](../evaluation-framework/README.md)
- [Prompt Patterns](../prompt-patterns/README.md)
- [Implementation Patterns](../implementation-patterns/README.md)
- [Intelligence Agents](../intelligence-agents/README.md)
- [Case Intelligence Agent](../intelligence-agents/case-intelligence-agent/README.md)
- [Threat Intelligence Agent](../intelligence-agents/threat-intelligence-agent/README.md)
- [Investigation Support Flow](../investigation-support-flow/README.md)
- [Conversational Copilot](../investigation-support-flow/06-conversational-copilot/README.md)

---

# Key Message

The specialist agents provide intelligence.

The Case Intelligence Agent provides investigation context.

The Investigation Orchestrator coordinates intelligence across the platform, determines which agents should contribute, and transforms individual intelligence capabilities into a unified Financial Crime Intelligence Platform.
