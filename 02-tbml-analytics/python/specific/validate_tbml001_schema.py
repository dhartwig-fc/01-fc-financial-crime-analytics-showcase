#!/usr/bin/env python3

from pathlib import Path
import pandas as pd
import sys

BASE_DIR = Path("python/specific/sample-data")
OUTPUT_DIR = BASE_DIR / "expected_outputs"

REQUIRED_FILES = [
    "customers.csv",
    "counterparties.csv",
    "entities.csv",
    "invoices.csv",
    "payments.csv",
    "relationships.csv",
    "shipping_documents.csv",
    "trades.csv",
]

OUTPUT_FILES = [
    "tbml001_alerts.csv",
    "tbml001_risk_scores.csv",
    "tbml001_investigation_queue.csv",
    "tbml001_intelligence_outputs.csv",
]


def check_exists():
    print("\nChecking input files...")
    for file in REQUIRED_FILES:
        path = BASE_DIR / file
        if not path.exists():
            raise FileNotFoundError(f"Missing input file: {path}")
        print(f"✓ {file}")

    print("\nChecking output files...")
    for file in OUTPUT_FILES:
        path = OUTPUT_DIR / file
        if not path.exists():
            raise FileNotFoundError(f"Missing output file: {path}")
        print(f"✓ {file}")


def check_required_columns():
    print("\nChecking required columns...")

    customers = pd.read_csv(BASE_DIR / "customers.csv")
    invoices = pd.read_csv(BASE_DIR / "invoices.csv")
    payments = pd.read_csv(BASE_DIR / "payments.csv")
    risks = pd.read_csv(OUTPUT_DIR / "tbml001_risk_scores.csv")

    required = {
        "customers": ["customer_id"],
        "invoices": ["transaction_id", "customer_id"],
        "payments": ["payment_id", "transaction_id"],
        "risk_scores": ["transaction_id", "risk_score"],
    }

    datasets = {
        "customers": customers,
        "invoices": invoices,
        "payments": payments,
        "risk_scores": risks,
    }

    for dataset_name, columns in required.items():
        df = datasets[dataset_name]

        for col in columns:
            if col not in df.columns:
                raise ValueError(
                    f"{dataset_name} missing required column {col}"
                )

        print(f"✓ {dataset_name}")


def check_primary_keys():
    print("\nChecking primary keys...")

    customers = pd.read_csv(BASE_DIR / "customers.csv")
    invoices = pd.read_csv(BASE_DIR / "invoices.csv")
    payments = pd.read_csv(BASE_DIR / "payments.csv")

    checks = [
        ("customers", customers, "customer_id"),
        ("invoices", invoices, "invoice_id"),
        ("payments", payments, "payment_id"),
    ]

    for name, df, key in checks:

        if df[key].isnull().any():
            raise ValueError(f"{name}: null values in {key}")

        if df[key].duplicated().any():
            raise ValueError(f"{name}: duplicate values in {key}")

        print(f"✓ {name}")


def check_foreign_keys():
    print("\nChecking foreign keys...")

    customers = pd.read_csv(BASE_DIR / "customers.csv")
    invoices = pd.read_csv(BASE_DIR / "invoices.csv")
    payments = pd.read_csv(BASE_DIR / "payments.csv")

    customer_ids = set(customers["customer_id"])

    bad_customers = invoices[
    ~invoices["customer_id"].isin(customer_ids)
]

    if len(bad_customers) > 0:
            raise ValueError(
            "Invoice contains unknown customer_id values"
       ) 

    invoice_transaction_ids = set(invoices["transaction_id"])
    payment_transaction_ids = set(payments["transaction_id"])

    if not payment_transaction_ids.issubset(invoice_transaction_ids):
        raise ValueError(
        "Payment contains unknown transaction_id values"
        )

    print("✓ Foreign keys valid")


def check_risk_scores():
    print("\nChecking risk scores...")

    risks = pd.read_csv(
        OUTPUT_DIR / "tbml001_risk_scores.csv"
    )

    if risks["risk_score"].min() < 0:
        raise ValueError("Risk score below 0")

    if risks["risk_score"].max() > 100:
        raise ValueError("Risk score above 100")

    print("✓ Risk scores valid")


def main():

    try:

        check_exists()
        check_required_columns()
        check_primary_keys()
        check_foreign_keys()
        check_risk_scores()

        print(
            "\n=================================="
        )
        print("TBML001 schema validation passed")
        print(
            "=================================="
        )

    except Exception as e:

        print("\nVALIDATION FAILED")
        print(e)

        sys.exit(1)


if __name__ == "__main__":
    main()
