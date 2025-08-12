import json
import azure.functions as func
from pathlib import Path

def main(req: func.HttpRequest) -> func.HttpResponse:
    data_dir = Path(__file__).resolve().parents[1]
    stations = json.loads((data_dir / "stations.json").read_text(encoding="utf-8"))
    q = (req.params.get("q") or "").lower()
    items = stations if not q else [s for s in stations if q in s["name"].lower()]
    return func.HttpResponse(json.dumps(items), mimetype="application/json")
