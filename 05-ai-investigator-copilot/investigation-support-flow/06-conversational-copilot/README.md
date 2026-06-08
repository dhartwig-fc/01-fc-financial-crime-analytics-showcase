# 06 Conversational Copilot

Transforming Investigation Intelligence into Interactive Investigator Decision Support

---

## Executive Summary

Conversational Copilot is the sixth and final operational capability within the AI Investigator Copilot architecture.

The capability enables investigators to interact directly with investigation intelligence using natural language.

Rather than manually reviewing multiple reports, evidence packs, case packages, and analytical outputs, investigators can engage with a conversational assistant capable of explaining findings, summarising evidence, answering investigative questions, and supporting decision-making.

The capability serves as the primary investigator interface to the broader Investigation Intelligence Platform.

---

## Capability Objective

The objective of Conversational Copilot is to:

- Accelerate investigator workflows
- Improve access to intelligence
- Reduce manual information retrieval
- Explain analytical findings
- Support investigative decision-making
- Improve consistency of investigations
- Increase investigator productivity

---

## Investigation Support Flow

```text
Analytics Detection
        ↓
Risk Scoring
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
        ↓
Conversational Copilot
        ↓
Investigator Decision
```

---

## Inputs

The capability consumes all intelligence products generated throughout the investigation lifecycle.

### Alert Rationales

- Alert explanations
- Risk drivers
- Typology indicators
- Recommended actions

### Investigator Summaries

- Case summaries
- Investigation priorities
- Key findings
- Risk assessments

### Evidence Packs

- Supporting evidence
- Customer intelligence
- Transaction information
- Network intelligence

### Intelligence Reports

- Intelligence assessments
- Investigation conclusions
- Recommended actions

### Case Packages

- Consolidated investigation artefacts
- Case documentation
- Escalation materials

### Analytics Outputs

- Risk scores
- Exposure scores
- Pattern detection outputs
- Network intelligence findings

---

## Processing Activities

### Context Retrieval

Retrieves relevant intelligence products and supporting evidence.

### Question Understanding

Interprets investigator requests.

### Evidence Grounding

Ensures responses remain linked to supporting evidence.

### Narrative Generation

Generates investigator-facing explanations and recommendations.

### Decision Support

Supports investigative analysis and review activities.

---

## Outputs

### Investigation Assistance

Provides contextual investigative support.

### Evidence Explanations

Explains supporting evidence.

### Risk Explanations

Explains risk indicators and analytical findings.

### Investigation Guidance

Suggests investigative next steps.

### Intelligence Summaries

Generates dynamic summaries of investigative findings.

### Draft Documentation

Supports report and narrative generation.

---

## Example Investigator Questions

### Alert Review

```text
Why was this alert generated?
```

```text
Which risk indicators contributed most to the score?
```

```text
What evidence supports the alert?
```

### Investigation Support

```text
What should I review first?
```

```text
Which counterparties are highest risk?
```

```text
Summarise this investigation.
```

```text
Explain the network exposure.
```

### Intelligence Review

```text
What are the key findings?
```

```text
What evidence supports this conclusion?
```

```text
How does this compare to previous cases?
```

### Reporting Support

```text
Draft an intelligence summary.
```

```text
Prepare a SAR narrative.
```

```text
Generate an executive briefing.
```

---

## Example Interaction

### Investigator

```text
Why is this customer considered high risk?
```

### Copilot

```text
The customer received a High Risk rating due to:

- Invoice inflation indicators identified
- Elevated trade value exposure
- High-risk jurisdiction involvement
- Associated network relationships

The strongest contributing factor was a 45%
variance between reported invoice values and
expected commodity benchmarks.

Supporting evidence is available within the
evidence package and trade documentation.

---

## Relationship to Case Package Generation

Conversational Copilot builds directly upon:

```text
05 Case Package Generation
```

The capability provides interactive access to investigation intelligence.

```text
Case Package
        ↓
Conversational Copilot
```

---

## Relationship to Financial Crime Analytics

The capability provides a unified interface across:

### Network Intelligence

- Relationship intelligence
- Entity networks
- Ownership structures

### TBML Analytics

- Trade anomalies
- Invoice manipulation indicators
- Commodity valuation findings

### Correspondent Banking Analytics

- Payment routing intelligence
- Nested banking findings
- Jurisdictional exposures

### Capital Markets Analytics

- Trading anomalies
- Market abuse indicators
- Behavioural intelligence

### Sanctions Exposure Analytics

- Exposure scores
- Ownership intelligence
- Screening findings

---

---

## External Intelligence Integration

The Conversational Copilot may also incorporate external threat intelligence to provide investigators with current typology context.

Examples include:

- Emerging sanctions evasion intelligence
- Shadow fleet activity
- Transshipment risk indicators
- High-risk jurisdiction developments
- New typology indicators
- Regulatory advisories
- Law enforcement intelligence alerts

External intelligence should not automatically change detection logic or scoring models.

Instead, it should support:

```text
External Intelligence
        ↓
Typology Context Enrichment
        ↓
Investigator Explanation
        ↓
Human Review
        ↓
Approved Model or Typology Update
```

## Reference Architecture Alignment

The Conversational Copilot operates across all architecture layers.

```text
Financial Crime Analytics
            ↓
Investigation Intelligence
            ↓
AI Investigator Copilot
            ↓
Conversational Copilot
            ↓
Investigator
```

The capability acts as the primary interface between investigators and generated intelligence.

## Threat Intelligence Agent

Future implementations may incorporate a dedicated Threat Intelligence Agent responsible for monitoring emerging financial crime threats and enriching investigative workflows with current typology intelligence.

The agent may consume:

- Regulatory advisories
- Law enforcement bulletins
- Industry intelligence reports
- Sanctions guidance
- Maritime intelligence
- Trade intelligence
- Open-source intelligence

### Example

External Intelligence:

```text
Emerging intelligence identifies increased
Iran-linked transshipment activity involving
shadow fleet vessels operating through new
maritime corridors.
```

Threat Intelligence Agent Assessment:

```text
Potential impact identified:

- Sanctions Exposure Analytics
- Maritime Risk Models
- Shadow Fleet Typologies
- Transshipment Detection Logic
```

Copilot Enrichment:

```text
This investigation aligns with emerging
shadow fleet transshipment behaviours
identified in recent maritime intelligence.

The vessel demonstrates routing patterns
consistent with newly identified sanctions
evasion methods.
```

### Potential Outputs

The Threat Intelligence Agent may:

- Enrich investigator explanations
- Generate typology update proposals
- Recommend scoring model reviews
- Recommend detection enhancements
- Identify emerging financial crime threats
- Support risk model governance

### Governance Requirement

Threat intelligence should not automatically modify production detection models.

Instead:

```text
External Intelligence
        ↓
Threat Intelligence Agent
        ↓
Typology Update Proposal
        ↓
Human Review
        ↓
Approved Model Change
```

Human approval remains mandatory before operational deployment of new detection logic or scoring methodologies.

---

## Governance Considerations

Conversational Copilot responses must:

- Remain evidence-based
- Maintain traceability
- Support auditability
- Avoid unsupported conclusions
- Preserve investigator accountability

Responses should always reference supporting evidence where available.

---

## Human-in-the-Loop Operating Model

The capability follows a Human-in-the-Loop approach.

```text
Investigator Question
          ↓
Copilot Response
          ↓
Investigator Review
          ↓
Investigator Decision
```

The Copilot supports decisions.

Investigators make decisions.

---

## Success Measures

The capability should improve:

- Investigation productivity
- Information accessibility
- Investigation speed
- Investigator consistency
- User satisfaction

Potential metrics include:

- Time saved per investigation
- Copilot utilisation rate
- Investigator acceptance rate
- Response quality scores
- Investigation cycle time reduction

---

## Future Enhancements

Future enhancements may include:

- Retrieval-Augmented Generation (RAG)
- Agentic investigation workflows
- Multi-agent orchestration
- Dynamic evidence retrieval
- Automated SAR drafting
- Case management integration
- Regulatory reporting assistants

---

## Navigation

- [AI Investigator Copilot](../../README.md)
- [Reference Architecture](../../reference-architecture/README.md)
- [Governance](../../governance/README.md)
- [05 Case Package Generation](../05-case-package-generation/README.md)

---

## Key Message

Conversational Copilot provides investigators with an interactive interface to investigation intelligence, transforming static intelligence products into dynamic decision-support capabilities that accelerate financial crime investigations while preserving human accountability.
```
