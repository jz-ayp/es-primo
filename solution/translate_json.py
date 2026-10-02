"""
Traducir el archivo de casos de prueba, en formato JSON, del formato de GitHub Classroom
al formato de Classroom 50.
"""

import json
from pathlib import Path

base_dir = Path(".")
f_in = base_dir / "solution" / "autograding.json"
f_out = base_dir / "solution" / "test_cases.json"

with f_in.open("r", encoding="utf-8") as file:
    tests_in = json.load(file)

clsrm50 = []
for test in tests_in["tests"]:
    clsrm50.append(
        {
            "name": test["name"],
            "type": "io",
            "run": "python3" + test["run"].split("python3")[1],
            "points": 1,
            "comparison": test["comparison"],
            "input": test["input"],
            "expected": test["output"],
        }
    )
clsrm50 = {"assignments": [{"tests": clsrm50}]}

with f_out.open("w", encoding="utf-8") as file:
    json.dump(clsrm50, file, indent=2, ensure_ascii=False)
          