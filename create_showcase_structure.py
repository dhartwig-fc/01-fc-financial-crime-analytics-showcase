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

readme_files = {
    "docs/README.md": "# Documentation\n\nArchitecture, methodology and governance notes.\n",
    "typologies/README.md": "# Typologies\n\nFinancial Crime typology catalogue and visual summaries.\n",
    "analytics-domains/README.md": "# Analytics Domains\n\nAnalytics domains covering network intelligence, 
TBML, sanctions, banking and capital markets.\n",
    "network-assets/README.md": "# Network Assets\n\nEntity resolution, beneficial ownership, relationship 
discovery and graph investigation assets.\n",
    "risk-scoring/README.md": "# Risk Scoring\n\nRisk indicators, scoring models, heatmaps and example 
outputs.\n",
    "investigator-workflows/README.md": "# Investigator Workflows\n\nAlert triage, case review, escalation, 
SAR support and AI copilot workflows.\n",
    "visualisations/README.md": "# Visualisations\n\nPlatform diagrams, typology maps, network graphs, 
workflow diagrams and screenshots.\n",
    "templates/README.md": "# Templates\n\nReusable templates for typologies, analytics use cases, network 
patterns and investigator playbooks.\n",
    "data/README.md": "# Data\n\nSynthetic or sample datasets only. No client, production or confidential 
data.\n",
    "notebooks/README.md": "# Notebooks\n\nPrototype notebooks and example analysis.\n",
    "src/README.md": "# Source Code\n\nReusable scoring, network, visualisation and utility scripts.\n",
}

for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)

    gitkeep = path / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")

for file_path, content in readme_files.items():
    path = ROOT / file_path
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text(content, encoding="utf-8")

print("Showcase repository folder structure created successfully.")
print(f"Root: {ROOT}")from 
pathlib 
import Path

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

readme_files = {
    "docs/README.md": "# Documentation\n\nArchitecture, methodology and governance notes.\n",
    "typologies/README.md": "# Typologies\n\nFinancial Crime typology catalogue and visual summaries.\n",
    "analytics-domains/README.md": "# Analytics Domains\n\nAnalytics domains covering network intelligence, 
TBML, sanctions, banking and capital markets.\n",
    "network-assets/README.md": "# Network Assets\n\nEntity resolution, beneficial ownership, relationship 
discovery and graph investigation assets.\n",
    "risk-scoring/README.md": "# Risk Scoring\n\nRisk indicators, scoring models, heatmaps and example 
outputs.\n",
    "investigator-workflows/README.md": "# Investigator Workflows\n\nAlert triage, case review, escalation, 
SAR support and AI copilot workflows.\n",
    "visualisations/README.md": "# Visualisations\n\nPlatform diagrams, typology maps, network graphs, 
workflow diagrams and screenshots.\n",
    "templates/README.md": "# Templates\n\nReusable templates for typologies, analytics use cases, network 
patterns and investigator playbooks.\n",
    "data/README.md": "# Data\n\nSynthetic or sample datasets only. No client, production or confidential 
data.\n",
    "notebooks/README.md": "# Notebooks\n\nPrototype notebooks and example analysis.\n",
    "src/README.md": "# Source Code\n\nReusable scoring, network, visualisation and utility scripts.\n",
}

for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)

    gitkeep = path / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")

for file_path, content in readme_files.items():
    path = ROOT / file_path
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text(content, encoding="utf-8")

print("Showcase repository folder structure created successfully.")
print(f"Root: {ROOT}")rm 
create_showcase_structure.py
open -e create_showcase_structure.py
