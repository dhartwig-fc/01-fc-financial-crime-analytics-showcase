# Relationship Discovery

> Network Intelligence Capability 02

Transforming isolated entities into connected intelligence networks.

---

## Executive Summary

Financial institutions often possess large volumes of customer, counterparty, payment, trade, and corporate information but lack visibility of the relationships connecting those entities across the enterprise.

Even when individual customers and organisations have been successfully resolved into trusted identities, investigators frequently struggle to understand how those entities interact with each other.

Relationship Discovery establishes the intelligence layer that connects entities through ownership, control, communication, transaction, geographic, and behavioural relationships.

By exposing these hidden connections, investigators can identify criminal networks, organised structures, intermediaries, beneficial ownership chains, and broader financial crime ecosystems that would otherwise remain undetected.

This capability transforms isolated customer records into actionable intelligence networks.

---

## Intelligence Outcome

Relationship Discovery enables investigators to:

- Identify hidden relationships between entities
- Discover previously unknown associates
- Reveal criminal and commercial networks
- Understand ownership and control structures
- Detect indirect connections between subjects
- Expand investigations beyond known entities
- Support network-based risk assessments
- Generate intelligence leads for further investigation

---

## Visual Intelligence Pattern

![NI002 Relationship Discovery Intelligence Pattern](../../images/network-intelligence-patterns/NI002_relationship-discovery/NI002_Relationship_Discovery_Intelligence_Pattern.png)

Relationship Discovery transforms trusted entities into connected intelligence networks.

Where Entity Resolution answers:

> "Who is this entity?"

Relationship Discovery answers:

> "Who are they connected to?"

---

# 1. Why Does The Problem Exist?

## Business Problem

Even after customer records have been successfully resolved into trusted identities, investigators frequently struggle to understand:

- Who controls an organisation
- Which entities are connected
- Whether hidden networks exist
- How money moves between participants
- Which counterparties operate together
- Whether criminal structures are present

As a result:

- Criminal structures remain hidden
- Investigations become manual
- Network risks are missed
- High-risk entities remain undiscovered
- Analysts review information in isolation

---

# 2. How Does Relationship Discovery Work?

## Analytical Stages

### Stage 1 – Trusted Entity Population

Relationship Discovery begins with a population of trusted entities generated through Entity Resolution.

Examples include:

- Customers
- Companies
- Directors
- Beneficial Owners
- Accounts
- Counterparties

Each entity possesses a trusted identity and unique identifier.

---

### Stage 2 – Relationship Identification

The platform identifies relationships between entities using multiple evidence sources.

#### Direct Relationships

- Ownership
- Directorship
- Shareholding
- Account Control
- Authorised Signatories

#### Contact Relationships

- Shared Address
- Shared Phone Number
- Shared Email Address

#### Financial Relationships

- Payment Flows
- Account Transfers
- Trade Transactions
- Correspondent Banking Activity

#### Behavioural Relationships

- Shared Devices
- Shared IP Addresses
- Shared Access Patterns
- Common Transaction Behaviour

---

### Stage 3 – Relationship Scoring

Relationships are evaluated and assigned confidence scores based on evidence quality.

Factors include:

- Evidence strength
- Data quality
- Relationship frequency
- Relationship duration
- Source reliability
- Number of corroborating indicators

The result is a trusted intelligence network.

---

### Stage 4 – Network Construction

Entities and relationships are assembled into a graph network.

The network contains:

- Nodes
- Edges
- Relationship Types
- Relationship Strength
- Investigation Context

The resulting graph becomes the foundation for advanced analytics.

---

# 3. What Intelligence Is Produced?

Relationship Discovery generates:

| Intelligence Output | Description |
|---------------------|-------------|
| Relationship Graphs | Visual representation of connected entities |
| Network Intelligence Nodes | Trusted entities connected through relationships |
| Relationship Scores | Confidence scoring for discovered links |
| Network Clusters | Groups of connected entities |
| Connected Counterparties | Known and previously unknown associates |
| Hidden Associate Intelligence | Newly discovered network participants |
| Ownership Structures | Connected ownership and control relationships |
| Investigation Leads | New investigative opportunities |
| Network Risk Inputs | Inputs for risk scoring and prioritisation |
| Beneficial Ownership Inputs | Foundation for ownership analytics |

---

# 4. How Do Investigators Use It?

## Investigation Example

An investigator begins with a single company subject.

Relationship Discovery reveals:

- Common directors
- Shared addresses
- Shared bank accounts
- Connected counterparties
- Historical payment relationships

Within minutes the investigator can identify:

- Additional entities requiring review
- Hidden ownership structures
- High-risk network participants
- Potential mule accounts
- Organised criminal networks

The investigation expands from a single entity into a complete intelligence network.

---

# 5. Business Value

## Investigation Benefits

- Faster investigations
- Improved lead generation
- Reduced manual analysis
- Better understanding of criminal structures
- Improved case quality

## Risk Benefits

- Improved detection of hidden risk
- Greater visibility of control structures
- Enhanced network analytics
- Better identification of organised activity

## Regulatory Benefits

- Stronger SAR investigations
- Improved AML controls
- Better auditability
- Enhanced explainability
- More effective regulatory reporting

---

# 6. Relationship Discovery Workflow

```mermaid
flowchart LR

A[Trusted Entity Population] --> B[Relationship Discovery]

B --> C1[Ownership Relationships]
B --> C2[Contact Relationships]
B --> C3[Financial Relationships]
B --> C4[Behavioural Relationships]

C1 --> D[Relationship Scoring]
C2 --> D
C3 --> D
C4 --> D

D --> E[Network Construction]

E --> F[Network Intelligence Graph]

F --> G1[Beneficial Ownership Analysis]
F --> G2[Network Risk Assessment]
F --> G3[Investigation Workflows]
F --> G4[AI Investigator Copilot]
```

---

# 7. Capability Dependencies

## Upstream Dependency

- NI001 – Entity Resolution Intelligence Pattern

## Downstream Capabilities Enabled

- NI003 – Beneficial Ownership Intelligence Pattern
- NI004 – Network Risk Assessment Intelligence Pattern
- NI005 – Investigation Workflow Intelligence Pattern

---

# 8. Network Intelligence Journey

```text
Entity Resolution
        ↓
Relationship Discovery
        ↓
Beneficial Ownership Analysis
        ↓
Network Risk Assessment
        ↓
Investigation Workflows
        ↓
AI Investigator Copilot
```

---

# Key Message

Entity Resolution answers:

> "Who is this entity?"

Relationship Discovery answers:

> "Who are they connected to?"

Together they establish the foundation of network intelligence and graph-based financial crime investigations.

---

# Navigation

⬅️ **Previous:** [Entity Resolution](../01-entity-resolution/README.md)

➡️ **Next:** [Beneficial Ownership Analysis](../03-beneficial-ownership/README.md)
