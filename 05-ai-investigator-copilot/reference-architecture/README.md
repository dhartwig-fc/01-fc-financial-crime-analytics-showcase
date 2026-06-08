# AI Investigator Copilot Reference Architecture

---

## Executive Summary

The AI Investigator Copilot Reference Architecture provides the enterprise architecture blueprint for transforming financial crime analytics into investigator-ready intelligence using generative AI.

The architecture sits above the Financial Crime Analytics Showcase and operationalises outputs from Network Intelligence, Trade-Based Money Laundering Analytics, Correspondent Banking Analytics, Capital Markets Analytics, and Sanctions Exposure Analytics.

Rather than replacing existing detection capabilities, AI Investigator Copilot converts risk signals, network intelligence, alerts, and investigative evidence into structured investigative artefacts that accelerate investigator decision-making.

The architecture provides a controlled framework for explainable, auditable, regulator-ready AI deployment across the financial crime investigation lifecycle.

---

# Architecture Vision

```text
Financial Crime Analytics
          ↓
Risk Detection
          ↓
Investigation Intelligence
          ↓
AI Investigator Copilot
          ↓
Investigator Decision Support
          ↓
Case Management
          ↓
Regulatory Outcomes
```

---

# Architectural Objectives

The architecture aims to:

- Accelerate investigator productivity
- Improve investigation consistency
- Reduce manual report writing
- Increase explainability
- Improve evidence utilisation
- Reduce investigation cycle times
- Support regulatory compliance
- Enable scalable investigator operations
- Standardise investigative outputs
- Preserve human accountability

---

# High-Level Architecture

```text
┌─────────────────────────────────────────────┐
│ FINANCIAL CRIME ANALYTICS LAYER             │
├─────────────────────────────────────────────┤
│ Network Intelligence                        │
│ TBML Analytics                              │
│ Correspondent Banking Analytics             │
│ Capital Markets Analytics                   │
│ Sanctions Exposure Analytics                │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│ INVESTIGATION INTELLIGENCE LAYER            │
├─────────────────────────────────────────────┤
│ Alerts                                      │
│ Risk Scores                                 │
│ Network Analysis                            │
│ Customer Intelligence                       │
│ Case Evidence                               │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│ AI INVESTIGATOR COPILOT LAYER               │
├─────────────────────────────────────────────┤
│ Prompt Framework                            │
│ LLM Services                                │
│ Retrieval Services                          │
│ Evidence Assembly                           │
│ Narrative Generation                        │
│ Reasoning Frameworks                        │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│ INVESTIGATOR SUPPORT LAYER                  │
├─────────────────────────────────────────────┤
│ Alert Rationales                            │
│ Investigator Summaries                      │
│ Evidence Packs                              │
│ Intelligence Reports                        │
│ Case Packages                               │
│ Conversational Copilot                      │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│ CASE MANAGEMENT & OPERATIONS                │
└─────────────────────────────────────────────┘
```

---

# Architectural Layers

## 1. Analytics Layer

The Analytics Layer produces the intelligence consumed by AI Investigator Copilot.

Sources include:

### Network Intelligence

Produces:

- Relationship intelligence
- Network typologies
- Entity connections
- Behavioural indicators

### TBML Analytics

Produces:

- Trade anomalies
- Commodity mismatches
- Invoice manipulation indicators
- Trade risk assessments

### Correspondent Banking Analytics

Produces:

- Nested banking indicators
- Payment routing risks
- Jurisdictional exposures
- Flow analysis

### Capital Markets Analytics

Produces:

- Market abuse indicators
- Insider trading signals
- Wash trading detection
- Manipulation patterns

### Sanctions Exposure Analytics

Produces:

- Exposure scores
- Sanctions network intelligence
- Ownership risks
- Screening intelligence

---

## 2. Investigation Intelligence Layer

This layer consolidates all investigative evidence.

Inputs include:

- Alerts
- Customer information
- Transaction history
- Risk scores
- Intelligence reports
- Network intelligence
- Historical investigations
- Supporting documentation

This becomes the evidence foundation for AI processing.

---

## 3. AI Investigator Copilot Layer

This layer transforms intelligence into investigator-ready outputs.

### Prompt Framework

Prompt engineering standards for:

- Investigation summaries
- Narrative generation
- Risk explanation
- Case packaging

### Retrieval Layer

Provides access to:

- Analytics outputs
- Evidence repositories
- Customer intelligence
- Historical investigations

### LLM Layer

Provides:

- Summarisation
- Explanation
- Narrative generation
- Question answering
- Investigation assistance

### Orchestration Layer

Coordinates:

- Prompt execution
- Data retrieval
- Response generation
- Output validation

---

## 4. Investigator Support Layer

This layer generates operational artefacts.

### Alert Rationale Generation

Explains why an alert was generated.

### Investigator Summary Generation

Creates investigator-ready briefings.

### Evidence Pack Generation

Assembles supporting evidence.

### Intelligence Report Generation

Creates structured intelligence reports.

### Case Package Generation

Builds regulator-ready case documentation.

### Conversational Copilot

Supports investigator interaction with intelligence.

---

# Governance Layer

Governance operates across all architectural layers.

```text
Governance
      │
      ├── Prompt Governance
      ├── Model Governance
      ├── Audit Controls
      ├── Monitoring
      ├── Human Oversight
      └── Compliance Controls
```

Governance ensures:

- Explainability
- Traceability
- Auditability
- Regulatory compliance

---

# Human-in-the-Loop Architecture

The architecture follows a Human-in-the-Loop operating model.

```text
Analytics
     ↓
AI Generation
     ↓
Investigator Review
     ↓
Investigator Decision
     ↓
Case Outcome
```

AI supports decisions.

Investigators make decisions.

---

# Data Flow

```text
Analytics Output
        ↓
Evidence Retrieval
        ↓
Prompt Assembly
        ↓
LLM Processing
        ↓
Generated Output
        ↓
Human Review
        ↓
Case Management
```

---

# Core Technology Components

| Component | Purpose |
|------------|----------|
| Analytics Platforms | Risk detection |
| Intelligence Repository | Evidence storage |
| Vector Database | Retrieval |
| Prompt Framework | AI instructions |
| LLM Platform | Generation |
| Orchestration Engine | Workflow management |
| Audit Store | Traceability |
| Case Management Platform | Investigation operations |

---

# Example Investigation Journey

```text
Network Intelligence Alert
            ↓
Risk Scoring
            ↓
Alert Rationale Generation
            ↓
Investigator Summary
            ↓
Evidence Pack
            ↓
Intelligence Report
            ↓
Case Package
            ↓
SAR / Escalation Decision
```

---

# Capability Relationships

```text
01 Alert Rationale Generation
                ↓
02 Investigator Summary Generation
                ↓
03 Evidence Pack Generation
                ↓
04 Intelligence Report Generation
                ↓
05 Case Package Generation
                ↓
06 Conversational Copilot
```

Each capability builds on the outputs of the previous capability.

---

# Future Architecture Evolution

Future enhancements may include:

- Agentic investigation workflows
- Multi-agent orchestration
- Autonomous evidence retrieval
- Automated typology generation
- Regulatory reporting assistants
- Investigation simulation environments

---

# Navigation

- [AI Investigator Copilot](../README.md)
- [Governance](../governance/README.md)
- [01 Alert Rationale Generation](../investigation-support-flow/01-alert-rationale-generation/README.md)
- [02 Investigator Summary Generation](../investigation-support-flow/02-investigator-summary-generation/README.md)
- [03 Evidence Pack Generation](../investigation-support-flow/03-evidence-pack-generation/README.md)
- [04 Intelligence Report Generation](../investigation-support-flow/04-intelligence-report-generation/README.md)
- [05 Case Package Generation](../investigation-support-flow/05-case-package-generation/README.md)
- [06 Conversational Copilot](../investigation-support-flow/06-conversational-copilot/README.md)

---

# Key Message

The AI Investigator Copilot Reference Architecture provides the blueprint for converting financial crime analytics into explainable, auditable, investigator-ready intelligence at enterprise scale.
