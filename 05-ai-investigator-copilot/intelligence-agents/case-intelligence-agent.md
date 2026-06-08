# Case Intelligence Agent

Connecting Domain Intelligence, Threat Intelligence and Investigation Context into a Unified Case View

---

# Executive Summary

The Case Intelligence Agent is the central reasoning capability within the AI Investigator Copilot architecture.

While specialist agents understand individual domains such as Network Intelligence, TBML, Correspondent Banking, Capital Markets, Sanctions and Threat Intelligence, the Case Intelligence Agent understands the investigation as a whole.

Its role is to consolidate all available intelligence into a unified case view, determine how different risk signals relate to one another, assess investigation relevance, and prepare the intelligence required for downstream investigator support workflows.

The Case Intelligence Agent becomes the bridge between specialist intelligence agents and the investigation support flow.

---

# Purpose

The purpose of the Case Intelligence Agent is to:

- Consolidate intelligence from multiple domains
- Determine which findings are relevant to the case
- Correlate risk indicators across analytics libraries
- Incorporate current threat intelligence
- Assemble a coherent case narrative
- Support investigation prioritisation
- Prepare intelligence for investigator-facing outputs

The agent does not replace the investigator.

It organises and explains the intelligence needed by the investigator.

---

# Position Within The AI Architecture

```text
Network Agent
TBML Agent
Correspondent Banking Agent
Capital Markets Agent
Sanctions Agent
Threat Intelligence Agent
        ↓
Case Intelligence Agent
        ↓
Investigation Support Flow
        ↓
Conversational Copilot
        ↓
Investigator
```

---

# Core Concept

Specialist agents understand domains.

The Case Intelligence Agent understands the case.

```text
Specialist Agents
        ↓
Domain Findings
        ↓
Case Intelligence Agent
        ↓
Unified Investigation View
```

This allows the platform to move from isolated findings to a coherent investigation narrative.

---

# Intelligence Sources

The Case Intelligence Agent may consume intelligence from:

- Network Intelligence Agent
- TBML Intelligence Agent
- Correspondent Banking Agent
- Capital Markets Agent
- Sanctions Agent
- Threat Intelligence Agent
- Alert Rationales
- Investigator Summaries
- Evidence Packs
- Intelligence Reports
- Case Packages
- Historical investigations
- Investigator feedback

---

# Case Intelligence Lifecycle

```text
Collect Intelligence
        ↓
Normalise Findings
        ↓
Correlate Risk Indicators
        ↓
Assess Case Relevance
        ↓
Prioritise Investigation Themes
        ↓
Generate Case Intelligence
        ↓
Support Investigator Outputs
```

---

# Cross-Domain Correlation

Example:

```text
TBML Agent
        ↓
Invoice inflation detected

Network Agent
        ↓
Shared ownership relationship identified

Sanctions Agent
        ↓
Indirect sanctions exposure detected

Threat Intelligence Agent
        ↓
Emerging shadow fleet typology identified
```

The Case Intelligence Agent correlates these findings:

```text
The case demonstrates indicators across
trade activity, ownership networks,
sanctions exposure and current threat
intelligence.
```

This creates a stronger investigative view than any single agent could provide alone.

---

# Threat Intelligence Integration

The Threat Intelligence Agent understands the external world.

The Case Intelligence Agent determines whether that external intelligence applies to the specific investigation.

```text
External Threat Intelligence
        ↓
Threat Intelligence Agent
        ↓
Case Intelligence Agent
        ↓
Case-Level Relevance Assessment
```
# Investigation Prioritisation

The Case Intelligence Agent helps prioritise investigation focus.

It may identify:

- Highest risk indicators
- Most important evidence
- Most relevant typologies
- Highest risk entities
- Highest risk counterparties
- Most urgent review areas

Example:

```text
Investigation Priority

1. Review ownership structure
2. Validate trade documentation
3. Assess sanctions exposure
4. Review counterparty relationships
5. Compare behaviour against emerging typology indicators
```

---

# Case Narrative Generation

The Case Intelligence Agent creates the foundation for a coherent case narrative.

Example:

```text
This case involves elevated financial crime risk
arising from trade activity, network relationships
and sanctions exposure.

The strongest indicators relate to invoice inflation,
opaque ownership and routing behaviour consistent
with emerging threat intelligence.
```

This narrative can then feed:

- Investigator Summaries
- Intelligence Reports
- Case Packages
- Conversational Copilot Responses

---

# Relationship to Investigation Support Flow

```text
Case Intelligence Agent
        ↓
Alert Rationale Generation
        ↓
Investigator Summary Generation
        ↓
Evidence Pack Generation
        ↓
Intelligence Report Generation
        ↓
Case Package Generation
```

The Case Intelligence Agent provides the case-level context needed to generate accurate and useful investigation artefacts.

---

# Relationship to Conversational Copilot

The Conversational Copilot uses Case Intelligence Agent outputs to answer investigator questions.

Example:

```text
Why is this case high risk?
```

The response may incorporate:

- Domain Intelligence
- Case Intelligence
- Threat Intelligence
- Evidence Pack Findings
- Risk Scoring Outputs

The Case Intelligence Agent ensures the response reflects the full investigation rather than a single analytic signal.

---

# Governance Considerations

The Case Intelligence Agent must:

- Remain evidence-based
- Preserve source traceability
- Avoid unsupported conclusions
- Separate facts from assessments
- Maintain auditability
- Support human review

The agent should not make final investigation decisions.

It should support investigator judgement.

---

# Navigation

- [AI Investigator Copilot](../README.md)
- [Reference Architecture](../reference-architecture/README.md)
- [Governance](../governance/README.md)
- [Evaluation Framework](../evaluation-framework/README.md)
- [Prompt Patterns](../prompt-patterns/README.md)
- [Implementation Patterns](../implementation-patterns/README.md)
- [Intelligence Agents](../intelligence-agents/README.md)
- [Threat Intelligence Agent](../intelligence-agents/threat-intelligence-agent/README.md)
- [Investigation Support Flow](../investigation-support-flow/README.md)
- [Conversational Copilot](../investigation-support-flow/06-conversational-copilot/README.md)

---

# Key Message

The Threat Intelligence Agent understands the external world.

The specialist analytics agents understand their domains.

The Case Intelligence Agent understands the investigation.

By consolidating domain intelligence, threat intelligence and investigation evidence into a unified case view, the Case Intelligence Agent becomes the central reasoning layer that enables intelligence-led financial crime investigations.
