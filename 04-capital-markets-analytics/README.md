# CBA001 – Nested Correspondent Banking Exposure

## Executive Summary

Nested correspondent banking occurs when a respondent bank gains indirect access to the international financial system through another correspondent relationship. This can create hidden exposure to high-risk jurisdictions, sanctioned entities, shell companies, or financial institutions that would otherwise be restricted from direct access.

This analytic pattern identifies nested correspondent banking relationships and traces payment flows across multiple intermediary institutions to reveal hidden exposure, concentration risk, and potential sanctions evasion pathways.

The capability enables investigators to understand indirect banking relationships that may not be visible through traditional transaction monitoring approaches.

---

## Visual Intelligence Pattern

![CBA001 Nested Correspondent Banking Exposure](images/CBA001_Nested_Correspondent_Banking_Exposure.png)

---

## Intelligence Question

Which payment flows traverse hidden or indirect correspondent banking relationships that expose the institution to elevated financial crime, sanctions, or regulatory risk?

---

## Pattern Objective

Identify respondent banks, intermediary institutions, and downstream beneficiaries operating through nested correspondent banking structures that may obscure the true origin, destination, or ownership of funds.

The pattern seeks to reveal:

- Hidden correspondent relationships
- Indirect access to the financial system
- High-risk jurisdiction exposure
- Sanctions evasion pathways
- Respondent bank concentration risk
- Complex payment routing structures

---

## Capability Dependencies

| Capability | Purpose |
|------------|----------|
| Entity Resolution | Resolve financial institutions across payment records |
| Network Intelligence | Identify indirect banking relationships |
| Payment Analytics | Analyse transaction flows |
| Sanctions Screening | Identify restricted entities and jurisdictions |
| Risk Scoring | Prioritise exposure scenarios |
| AI Investigator Copilot | Support investigator decision making |

---

## Downstream Capabilities Enabled

- Correspondent Risk Scoring
- Sanctions Exposure Analytics
- Network Intelligence
- Enhanced Due Diligence
- AI Investigator Copilot
- Regulatory Reporting
- Alert Prioritisation

---

## Lifecycle Diagram

```text
Payment Messages
        ↓
Institution Resolution
        ↓
Correspondent Network Construction
        ↓
Nested Relationship Detection
        ↓
Exposure Analysis
        ↓
Risk Scoring
        ↓
Investigator Review
```

---

## How It Works

The capability analyses payment records, correspondent banking relationships, SWIFT messages, and institution reference data.

The process:

1. Identify originating institutions.
2. Resolve intermediary correspondents.
3. Map downstream respondent banks.
4. Construct payment routing networks.
5. Detect nested access arrangements.
6. Assess jurisdictional and sanctions exposure.
7. Score correspondent banking risk.
8. Generate investigator intelligence.

---

## Data Sources

### Internal Sources

- SWIFT MT Messages
- SWIFT MX Messages
- Payment Transactions
- Customer Data
- Correspondent Banking Reference Data
- KYC Records

### External Sources

- Sanctions Lists
- High-Risk Jurisdiction Lists
- Bank Ownership Data
- Corporate Registry Data
- Adverse Media Sources

---

## Analytics Techniques

### Network Analysis

Construct multi-hop correspondent banking networks to identify indirect relationships.

### Path Analysis

Trace payment routes across multiple institutions.

### Concentration Analysis

Measure dependency on specific correspondent institutions.

### Exposure Analysis

Identify downstream exposure to elevated-risk entities and jurisdictions.

### Risk Scoring

Assign risk scores based on:

- Jurisdiction risk
- Institution risk
- Network complexity
- Payment volume
- Sanctions proximity

---

## Intelligence Produced

The capability generates:

- Nested correspondent banking relationships
- Hidden institution exposure
- High-risk payment corridors
- Sanctions adjacency indicators
- Correspondent concentration risks
- Downstream beneficiary exposure

---

## Example Scenario

A payment originates from Bank A.

The transaction passes through:

```text
Bank A
   ↓
Correspondent Bank X
   ↓
Correspondent Bank Y
   ↓
Respondent Bank Z
   ↓
Beneficiary
```

Traditional monitoring may only assess Bank X.

This capability identifies the complete payment chain and reveals that Respondent Bank Z operates within a sanctioned or elevated-risk jurisdiction.

The institution gains visibility of exposure that would otherwise remain hidden.

---

## How Investigators Use It

Investigators use the intelligence to:

- Understand payment routing structures
- Identify hidden correspondent relationships
- Assess sanctions exposure
- Support enhanced due diligence reviews
- Investigate unusual payment flows
- Prioritise high-risk alerts

---

## Business Benefits

### Risk Reduction

Improves visibility into indirect exposure and hidden banking relationships.

### Regulatory Compliance

Supports correspondent banking expectations and sanctions obligations.

### Operational Efficiency

Provides investigators with pre-built relationship intelligence.

### Enhanced Transparency

Reveals payment routes that are not visible through traditional monitoring approaches.

---

## Correspondent Banking Intelligence Journey

```text
Payment Data
        ↓
Institution Resolution
        ↓
Network Construction
        ↓
Nested Relationship Detection
        ↓
Risk Assessment
        ↓
Investigator Intelligence
        ↓
Operational Action
```

---

## Navigation

### Previous

- Financial Crime Analytics Showcase

### Related Capabilities

- Network Intelligence
- Sanctions Exposure Analytics
- AI Investigator Copilot
- Entity Resolution Analytics

### Next

- CBA002 High-Risk Corridor Analysis

---

## Key Message

Nested correspondent banking relationships can conceal exposure to elevated-risk institutions, jurisdictions, and sanctioned entities. By combining payment analytics, network intelligence, and risk scoring, investigators gain visibility into hidden banking relationships and indirect financial crime exposure across complex international payment networks.
