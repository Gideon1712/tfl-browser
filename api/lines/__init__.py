import json
import azure.functions as func
from pathlib import Path

def main(req: func.HttpRequest) -> func.HttpResponse:
    data_dir = Path(__file__).resolve().parents[1]
    lines = json.loads((data_dir / "lines.json").read_text(encoding="utf-8"))
    return func.HttpResponse(json.dumps(lines), mimetype="application/json")
