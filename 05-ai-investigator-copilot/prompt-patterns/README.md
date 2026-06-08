# Prompt Patterns

Designing Explainable, Repeatable and Governed Prompt Architectures for Financial Crime Intelligence

---

# Executive Summary

Prompt Patterns define how the AI Investigator Copilot transforms financial crime analytics, investigation intelligence and threat intelligence into investigator-ready outputs.

Rather than relying on ad-hoc prompts, the platform uses structured prompt architectures designed to ensure consistency, explainability, auditability and investigator value.

Prompt Patterns act as the reasoning framework that connects analytics, intelligence and evidence to AI-generated outputs.

The objective is to ensure that AI-generated intelligence remains grounded in evidence, aligned with investigative workflows and compliant with governance requirements.

---

# Purpose

Prompt Patterns provide a standardised approach for:

- Alert explanation
- Investigation support
- Intelligence synthesis
- Evidence interpretation
- Case documentation
- Threat intelligence enrichment
- Investigator decision support

The framework ensures prompts remain consistent across all AI Investigator Copilot capabilities.

---

# Prompt Architecture

The platform follows a structured prompt lifecycle.

```text
Analytics
        ↓

Investigation Intelligence

        ↓

Prompt Assembly

        ↓

LLM Processing

        ↓

Generated Intelligence

        ↓

Human Review
```

Prompt assembly becomes a controlled process rather than an ad-hoc interaction.

---

# Prompt Engineering Principles

All prompts should follow five core principles.

## Grounded

Responses must remain linked to evidence.

---

## Explainable

Reasoning should be understandable.

---

## Traceable

Outputs should be auditable.

---

## Consistent

Prompts should generate repeatable outputs.

---

## Investigator-Focused

Outputs should support investigation workflows.

---

# Prompt Components

Each prompt consists of structured context blocks.

```text
System Instructions
        +
Investigation Context
        +
Analytics Context
        +
Evidence Context
        +
Threat Intelligence Context
        +
User Request
```

The LLM receives assembled intelligence rather than raw data.

---

# Prompt Lifecycle

```text
Investigator Question
          ↓

Context Retrieval
          ↓

Prompt Assembly
          ↓

LLM Processing
          ↓

Response Generation
          ↓

Human Review
```

This lifecycle forms the foundation of AI Investigator Copilot interactions.

---

# Grounding Pattern

Grounding ensures outputs remain evidence-based.

Example:

```text
Customer Risk Score: 82

Risk Drivers:

- Invoice inflation
- High-risk jurisdiction
- Network exposure

Evidence:

- Invoice records
- Trade documentation
- Counterparty information
```

Prompt:

```text
Explain why the customer received a high-risk rating.

Only use the supplied evidence.

Do not create unsupported conclusions.
```

Grounding reduces hallucination risk and improves explainability.

---

# Alert Rationale Prompt Pattern

Purpose:

Explain why an alert was generated.

Inputs:

- Alert
- Risk Score
- Risk Drivers
- Evidence

Outputs:

- Alert explanation
- Risk rationale
- Investigator guidance

Example:

```text
Explain why this alert was generated.

Summarise key risk drivers.

Reference supporting evidence.

Suggest areas for investigator review.
```

---

# Investigator Summary Prompt Pattern

Purpose:

Generate concise investigator briefings.

Inputs:

- Alert rationale
- Risk findings
- Evidence

Outputs:

- Investigation summary
- Key findings
- Investigation priorities

Example:

```text
Generate an investigator summary.

Focus on suspicious activity,
risk indicators and investigative priorities.

Keep the summary concise and actionable.
```

---

# Evidence Pack Prompt Pattern

Purpose:

Organise evidence into structured investigation packages.

Inputs:

- Customer information
- Transactions
- Network intelligence
- Supporting documents

Outputs:

- Structured evidence package
- Supporting evidence references

Example:

```text
Organise the available evidence
into a structured investigation package.

Group evidence by category.

Highlight key supporting information.
```

---

# Intelligence Report Prompt Pattern

Purpose:

Generate investigation intelligence products.

Inputs:

- Alert rationale
- Investigator summary
- Evidence pack

Outputs:

- Executive summary
- Intelligence findings
- Risk assessment
- Recommendations

Example:

```text
Generate a structured intelligence report.

Explain findings.

Reference supporting evidence.

Provide investigator recommendations.
```

---

# Case Package Prompt Pattern

Purpose:

Generate investigation-ready case documentation.

Inputs:

- Intelligence report
- Evidence package
- Investigation findings

Outputs:

- Case package
- Investigation artefacts
- Escalation materials

Example:

```text
Create a complete investigation case package.

Include executive summary,
findings, evidence references
and recommended actions.
```

---

# Threat Intelligence Enrichment Pattern

Purpose:

Incorporate emerging threat intelligence into investigations.

Inputs:

- Investigation context
- Threat intelligence
- Typology intelligence

Outputs:

- Intelligence enrichment
- Threat context
- Emerging risk indicators

Example:

```text
Explain whether the investigation
aligns with emerging threat intelligence.

Reference relevant typologies.

Highlight any newly identified risks.
```

---

# Multi-Agent Prompt Pattern

Future architectures may support multiple specialist agents.

Example:

```text
Network Agent
        +
TBML Agent
        +
Sanctions Agent
        +
Case Intelligence Agent
        +
Threat Intelligence Agent
```

Outputs from multiple agents are combined before final response generation.

```text
Specialist Intelligence
          ↓

Prompt Assembly
          ↓

Response Generation
```

---

# Prompt Governance

All prompts should support:

- Explainability
- Traceability
- Auditability
- Human review
- Regulatory defensibility

Prompt changes should follow formal governance processes.

---

# Prompt Version Management

Prompts should be version controlled.

Example:

```text
Prompt v1.0

Prompt v1.1

Prompt v2.0
```

Version control supports:

- Auditability
- Testing
- Rollback
- Improvement tracking

---

# Future Prompt Architecture

Future enhancements may include:

- Dynamic prompt generation
- Retrieval-Augmented Generation (RAG)
- Agent-specific prompt templates
- Threat intelligence prompt enrichment
- Adaptive prompting
- Multi-agent orchestration prompts

These capabilities will enable increasingly sophisticated AI investigation workflows.

---

## Navigation

- [AI Investigator Copilot](../README.md)
- [Reference Architecture](../reference-architecture/README.md)
- [Governance](../governance/README.md)
- [Evaluation Framework](../evaluation-framework/README.md)
- [Implementation Patterns](../implementation-patterns/README.md)

---

# Key Message

Prompt Patterns provide the reasoning framework that transforms analytics, investigation intelligence and threat intelligence into consistent, explainable and investigator-focused AI outputs.

By standardising prompt design across the platform, the AI Investigator Copilot delivers repeatable, auditable and evidence-based intelligence products that support effective financial crime investigations.
