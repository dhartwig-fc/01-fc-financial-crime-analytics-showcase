from pathlib import Path

ROOT = Path.cwd()

folders = [
    "images",
    "docs",
    "docs/architecture",
    "docs/methodology",
    "docs/governance",
    "typologies",
    "typologies/network-intelligence",
    "typologies/tbml",
    "typologies/sanctions",
    "typologies/banking",
    "typologies/capital-markets",
from pathlib import Path

ROOT = Path.cwd()

folders = [
    "images",
    "docs",
    "docs/architecture",
    "docs/methodology",
    "docs/governance",
    "typologies",
    "typologies/network-intelligence",
    "typologies/tbml",
    "typologies/sanctions",
    "typologies/banking",
    "typologies/capital-markets",
    "typologies/mule-networks",
    "typologies/correspondent-banking",
    "typologies/emerging-threats",
    "analytics-domains",
    "analytics-domains/network-intelligence",
    "analytics-domains/tbml-analytics",
    "analytics-domains/sanctions-exposure-analytics",
    "analytics-domains/banking-analytics",
    "analytics-domains/capital-markets-analytics",
    "network-assets",
    "network-assets/entity-resolution",
    "network-assets/beneficial-ownership",
    "network-assets/relationship-discovery",
    "network-assets/graph-investigation-patterns",
    "network-assets/network-risk-scoring",
    "risk-scoring",
    "risk-scoring/scoring-models",
    "risk-scoring/risk-indicators",
    "risk-scoring/heatmaps",
    "risk-scoring/example-outputs",
    "investigator-workflows",
    "investigator-workflows/alert-triage",
    "investigator-workflows/case-review",
    "investigator-workflows/escalation",
    "investigator-workflows/sar-support",
    "investigator-workflows/ai-copilot",
    "visualisations",
    "visualisations/platform-overview",
    "visualisations/typology-maps",
    "visualisations/network-graphs",
    "visualisations/workflow-diagrams",
    "visualisations/risk-scoring",
    "visualisations/screenshots",
    "templates",
    "templates/typology-template",
    "templates/analytics-use-case-template",
    "templates/network-pattern-template",
    "templates/investigator-playbook-template",
    "data",
    "data/sample",
    "data/synthetic",
    "data/reference",
    "notebooks",
    "notebooks/examples",
    "notebooks/prototypes",
    "src",
    "src/scoring",
    "src/network",
    "src/visualisation",
    "src/utils",
]

for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)
    gitkeep = path / ".gitkeep"
    gitkeep.touch(exist_ok=True)

print("Showcase repository folder structure created successfully.")
print(f"Root: {ROOT}")
