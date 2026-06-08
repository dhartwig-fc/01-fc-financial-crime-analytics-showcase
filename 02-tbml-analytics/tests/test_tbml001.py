import subprocess


def test_tbml001_schema_validator_runs_successfully():

    result = subprocess.run(
        [
            "python3",
            "python/specific/validate_tbml001_schema.py"
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "TBML001 schema validation passed" in result.stdout
