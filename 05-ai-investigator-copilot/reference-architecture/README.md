# AI Investigator Copilot Reference Architecture

## Executive Summary

The AI Investigator Copilot is designed as a human-in-the-loop investigation support capability for financial crime teams.

It helps investigators gather evidence, understand customer risk, review network intelligence, summarise case context and prepare investigation outputs.

The Copilot does not replace investigator judgement. It provides structured support by consuming trusted intelligence outputs from the wider Financial Crime Analytics architecture.

---

## Architecture Purpose

The purpose of this reference architecture is to show how an AI Investigator Copilot can be safely connected to financial crime data, analytics and investigation workflows.

The architecture is designed to support:

- Alert triage
- Case summarisation
- Customer risk review
- Transaction explanation
- Network intelligence interpretation
- Beneficial ownership review
- Investigation workflow support
- Human decision-making

---

## Core Design Principle

The Copilot should not reason directly over raw, ungoverned data.

Instead, it should consume a structured Case Intelligence Model built from trusted upstream capabilities.

This reduces hallucination risk, improves explainability and makes the Copilot more suitable for regulated financial crime environments.

---

## High-Level Architecture

```mermaid
flowchart TD

A[Financial Crime Data Sources] --> B[Data Preparation Layer]
B --> C[Network Intelligence Layer]
C --> D[Case Intelligence Model]
D --> E[AI Investigator Copilot]
E --> F[Investigator Review]
F --> G[Investigation Decision]

A1[Customer Data] --> A
A2[Transaction Data] --> A
A3[Case History] --> A
A4[Sanctions Data] --> A
A5[Policy & Procedure Documents] --> A

C1[Entity Resolution] --> C
C2[Relationship Discovery] --> C
C3[Beneficial Ownership Intelligence] --> C
C4[Network Risk Assessment] --> C
C5[Investigation Workflow Intelligence] --> C

E1[LLM Reasoning Layer] --> E
E2[RAG Knowledge Layer] --> E
E3[Tool Calling Layer] --> E
E4[Prompt Guardrails] --> E

F --> H[Case Notes]
F --> I[Escalation]
F --> J[EDD Recommendation]
F --> K[SAR Consideration]
