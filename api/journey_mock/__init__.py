import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    src = req.params.get("from")
    dst = req.params.get("to")
    if not src or not dst:
        return func.HttpResponse(json.dumps({"error": "from and to are required"}), status_code=400, mimetype="application/json")
    mid = "Oxford Circus" if src != "Oxford Circus" and dst != "Oxford Circus" else "Green Park"
    payload = {"from": src, "to": dst, "stops": [src, mid, dst], "duration_min": 10}
    return func.HttpResponse(json.dumps(payload), mimetype="application/json")
