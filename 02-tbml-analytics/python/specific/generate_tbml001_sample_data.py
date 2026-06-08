from pathlib import Path
import pandas as pd

BASE_DIR = Path("sample-data")
OUTPUT_DIR = BASE_DIR / "expected_outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# ENTITIES
# --------------------------------------------------

entities = pd.DataFrame([
    [
        "ENT001",
        "ABC Imports Ltd",
        "Company",
        "United Kingdom",
        "United Kingdom",
        "Industrial Equipment",
        72,
        "High"
    ],
    [
        "ENT002",
        "XYZ Trading LLC",
        "Company",
        "United Arab Emirates",
        "United Arab Emirates",
        "Electronics Trading",
        81,
        "High"
    ],
    [
        "ENT003",
        "Global Holdings FZE",
        "Company",
        "United Arab Emirates",
        "United Arab Emirates",
        "Holding Company",
        78,
        "High"
    ],
    [
        "ENT004",
        "Normal Machinery GmbH",
        "Company",
        "Germany",
        "Germany",
        "Machinery Manufacturing",
        28,
        "Low"
    ],
    [
        "ENT005",
        "Standard Imports Ltd",
        "Company",
        "United Kingdom",
        "United Kingdom",
        "Industrial Equipment",
        35,
        "Low"
    ]
],
columns=[
    "entity_id",
    "entity_name",
    "entity_type",
    "incorporation_country",
    "operating_country",
    "industry_sector",
    "risk_score",
    "risk_band"
])

# --------------------------------------------------
# CUSTOMERS
# --------------------------------------------------

customers = pd.DataFrame([
    [
        "CUST001",
        "ENT001",
        "ABC Imports Ltd",
        72,
        "High",
        900000,
        2500000,
        "United Kingdom",
        "Industrial Equipment",
        True
    ],
    [
        "CUST002",
        "ENT005",
        "Standard Imports Ltd",
        35,
        "Low",
        1200000,
        1180000,
        "United Kingdom",
        "Industrial Equipment",
        False
    ]
],
columns=[
    "customer_id",
    "entity_id",
    "customer_name",
    "customer_risk_score",
    "customer_risk_band",
    "expected_monthly_volume",
    "actual_monthly_volume",
    "country_of_operation",
    "industry_sector",
    "related_party_trade_flag"
])

# --------------------------------------------------
# COUNTERPARTIES
# --------------------------------------------------

counterparties = pd.DataFrame([
    [
        "CP001",
        "ENT002",
        "XYZ Trading LLC",
        81,
        "High",
        "United Arab Emirates",
        "United Arab Emirates",
        38,
        True,
        True
    ],
    [
        "CP002",
        "ENT004",
        "Normal Machinery GmbH",
        28,
        "Low",
        "Germany",
        "Germany",
        86,
        False,
        False
    ]
],
columns=[
    "counterparty_id",
    "entity_id",
    "counterparty_name",
    "counterparty_risk_score",
    "counterparty_risk_band",
    "incorporation_country",
    "operating_country",
    "commercial_footprint_score",
    "shell_company_indicator",
    "related_party_flag"
])

# --------------------------------------------------
# RELATIONSHIPS
# --------------------------------------------------

relationships = pd.DataFrame([
    [
        "REL001",
        "ENT001",
        "ENT002",
        "Beneficial Owner",
        87,
        True,
        True,
        True,
        88
    ],
    [
        "REL002",
        "ENT001",
        "ENT003",
        "Ownership",
        84,
        True,
        True,
        False,
        82
    ],
    [
        "REL003",
        "ENT005",
        "ENT004",
        "Trade",
        42,
        False,
        False,
        False,
        25
    ]
],
columns=[
    "relationship_id",
    "source_entity_id",
    "target_entity_id",
    "relationship_type",
    "relationship_confidence_score",
    "related_party_trade_flag",
    "shared_owner_flag",
    "shared_director_flag",
    "relationship_risk_score"
])

# --------------------------------------------------
# TRADES
# --------------------------------------------------

trades = pd.DataFrame([
    [
        "TRD001",
        "CUST001",
        "CP001",
        "2026-02-14",
        2500000,
        "USD",
        "851762",
        "Network communications equipment",
        "United Arab Emirates",
        "United Kingdom",
        True,
        42
    ],
    [
        "TRD002",
        "CUST002",
        "CP002",
        "2026-02-18",
        1180000,
        "USD",
        "842890",
        "Industrial machinery",
        "Germany",
        "United Kingdom",
        False,
        82
    ]
],
columns=[
    "transaction_id",
    "customer_id",
    "counterparty_id",
    "transaction_date",
    "transaction_value",
    "transaction_currency",
    "commodity_code",
    "commodity_description",
    "origin_country",
    "destination_country",
    "high_risk_corridor_flag",
    "commercial_rationale_score"
])
# --------------------------------------------------
# INVOICES
# --------------------------------------------------

invoices = pd.DataFrame([
    [
        "INV001",
        "TRD001",
        "CUST001",
        "CP001",
        2500000,
        "USD",
        "851762",
        1000,
        2500,
        "2026-02-14"
    ],
    [
        "INV002",
        "TRD002",
        "CUST002",
        "CP002",
        1180000,
        "USD",
        "842890",
        100,
        11800,
        "2026-02-18"
    ]
],
columns=[
    "invoice_id",
    "transaction_id",
    "customer_id",
    "counterparty_id",
    "invoice_value",
    "invoice_currency",
    "commodity_code",
    "quantity",
    "unit_price",
    "invoice_date"
])

# --------------------------------------------------
# MARKET BENCHMARKS
# --------------------------------------------------

market_benchmarks = pd.DataFrame([
    [
        "BMK001",
        "851762",
        1700,
        1700000,
        "USD",
        86,
        "2026-02-10",
        88,
        42
    ],
    [
        "BMK002",
        "842890",
        11500,
        1150000,
        "USD",
        91,
        "2026-02-12",
        90,
        61
    ]
],
columns=[
    "benchmark_id",
    "commodity_code",
    "benchmark_unit_price",
    "benchmark_value",
    "benchmark_currency",
    "benchmark_confidence_score",
    "benchmark_date",
    "source_reliability_score",
    "comparable_trade_count"
])

# --------------------------------------------------
# PAYMENTS
# --------------------------------------------------

payments = pd.DataFrame([
    [
        "PAY001",
        "TRD001",
        2500000,
        "2026-03-10",
        "USD",
        True,
        False,
        False
    ],
    [
        "PAY002",
        "TRD002",
        1180000,
        "2026-03-12",
        "USD",
        True,
        False,
        False
    ]
],
columns=[
    "payment_id",
    "transaction_id",
    "payment_amount",
    "payment_date",
    "payment_currency",
    "payment_match_flag",
    "third_party_payment_flag",
    "split_payment_flag"
])

# --------------------------------------------------
# SHIPPING DOCUMENTS
# --------------------------------------------------

shipping_documents = pd.DataFrame([
    [
        "SHIP001",
        "TRD001",
        "BOL001",
        "United Arab Emirates",
        "United Kingdom",
        "Jebel Ali → Rotterdam → Felixstowe",
        "Moderate",
        True
    ],
    [
        "SHIP002",
        "TRD002",
        "BOL002",
        "Germany",
        "United Kingdom",
        "Hamburg → Felixstowe",
        "Strong",
        False
    ]
],
columns=[
    "shipment_id",
    "transaction_id",
    "bill_of_lading_id",
    "origin_country",
    "destination_country",
    "shipping_route",
    "documentation_quality",
    "document_discrepancy_flag"
])

# --------------------------------------------------
# BUILD ANALYTICS DATASET
# --------------------------------------------------

merged = (
    trades
    .merge(
        invoices,
        on=[
            "transaction_id",
            "customer_id",
            "counterparty_id",
            "commodity_code"
        ]
    )
    .merge(
        market_benchmarks,
        on="commodity_code"
    )
    .merge(
        customers[
            [
                "customer_id",
                "customer_risk_score"
            ]
        ],
        on="customer_id"
    )
    .merge(
        counterparties[
            [
                "counterparty_id",
                "counterparty_risk_score",
                "related_party_flag",
                "shell_company_indicator"
            ]
        ],
        on="counterparty_id"
    )
)

# --------------------------------------------------
# CALCULATED FIELDS
# --------------------------------------------------

merged["variance_amount"] = (
    merged["invoice_value"]
    - merged["benchmark_value"]
)

merged["variance_pct"] = (
    (
        merged["invoice_value"]
        - merged["benchmark_value"]
    )
    / merged["benchmark_value"]
) * 100

merged["over_invoice_flag"] = (
    merged["variance_pct"] > 30
)

# --------------------------------------------------
# RISK SCORING
# --------------------------------------------------

def calculate_risk_score(row):

    score = 0

    score += min(row["variance_pct"], 60) * 0.60

    score += (
        row["customer_risk_score"] * 0.20
    )

    score += (
        row["counterparty_risk_score"] * 0.20
    )

    if row["related_party_flag"]:
        score += 15

    if row["high_risk_corridor_flag"]:
        score += 10

    if row["shell_company_indicator"]:
        score += 10

    return min(round(score), 100)

merged["risk_score"] = (
    merged.apply(
        calculate_risk_score,
        axis=1
    )
)

def risk_band(score):

    if score >= 90:
        return "Critical"

    if score >= 70:
        return "High"

    if score >= 40:
        return "Medium"

    return "Low"

merged["risk_band"] = (
    merged["risk_score"]
    .apply(risk_band)
)

merged["alert_flag"] = (
    merged["over_invoice_flag"]
    &
    (merged["risk_score"] >= 70)
)

# --------------------------------------------------
# ALERT OUTPUT
# --------------------------------------------------

alerts = (
    merged[
        merged["alert_flag"]
    ]
    .copy()
)

alerts["alert_id"] = [
    f"ALT{i:03d}"
    for i in range(
        1,
        len(alerts) + 1
    )
]

tbml001_alerts = alerts[
    [
        "alert_id",
        "transaction_id",
        "customer_id",
        "counterparty_id",
        "invoice_value",
        "benchmark_value",
        "variance_pct",
        "risk_score",
        "risk_band",
        "alert_flag"
    ]
]

# --------------------------------------------------
# RISK SCORE OUTPUT
# --------------------------------------------------

tbml001_risk_scores = merged[
    [
        "transaction_id",
        "customer_id",
        "counterparty_id",
        "variance_pct",
        "risk_score",
        "risk_band"
    ]
]

# --------------------------------------------------
# INVESTIGATION QUEUE
# --------------------------------------------------

tbml001_investigation_queue = (
    tbml001_alerts.copy()
)

tbml001_investigation_queue[
    "priority"
] = tbml001_investigation_queue[
    "risk_score"
].apply(
    lambda x:
    "Priority 1"
    if x >= 90
    else "Priority 2"
)

tbml001_investigation_queue[
    "recommended_action"
] = (
    "Enhanced Due Diligence"
)

# --------------------------------------------------
# INTELLIGENCE OUTPUTS
# --------------------------------------------------

tbml001_intelligence_outputs = pd.DataFrame([
    [
        "INT001",
        "ALT001",
        "TBML001 Intelligence Report",
        "Invoice inflation detected with related-party indicators and elevated trade corridor risk.",
        "Investigator Brief; Evidence Pack; Risk Assessment; Case Summary"
    ]
],
columns=[
    "intelligence_output_id",
    "alert_id",
    "output_type",
    "summary",
    "products_generated"
])

# --------------------------------------------------
# WRITE INPUT FILES
# --------------------------------------------------

datasets = {
    "entities.csv": entities,
    "customers.csv": customers,
    "counterparties.csv": counterparties,
    "relationships.csv": relationships,
    "trades.csv": trades,
    "invoices.csv": invoices,
    "market_benchmarks.csv": market_benchmarks,
    "payments.csv": payments,
    "shipping_documents.csv": shipping_documents
}

for filename, dataframe in datasets.items():
    dataframe.to_csv(
        BASE_DIR / filename,
        index=False
    )
# --------------------------------------------------
# WRITE OUTPUT FILES
# --------------------------------------------------

outputs = {
    "tbml001_alerts.csv": tbml001_alerts,
    "tbml001_risk_scores.csv": tbml001_risk_scores,
    "tbml001_investigation_queue.csv": tbml001_investigation_queue,
    "tbml001_intelligence_outputs.csv": tbml001_intelligence_outputs
}

for filename, dataframe in outputs.items():
    dataframe.to_csv(
        OUTPUT_DIR / filename,
        index=False
    )

print(
    "TBML001 sample data pack generated successfully."
)

print(
    f"Input files written to: {BASE_DIR}"
)

print(
    f"Output files written to: {OUTPUT_DIR}"
)
