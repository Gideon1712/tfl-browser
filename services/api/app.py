import json, time
from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
with open("stations.json","r",encoding="utf-8-sig") as f: STATIONS=json.load(f)
with open("lines.json","r",encoding="utf-8-sig") as f: LINES=json.load(f)

REQ_COUNT = Counter("http_requests_total","Total HTTP requests",["endpoint","method","code"])
REQ_LAT   = Histogram("http_request_duration_seconds","Latency",["endpoint","method"])

@app.before_request
def _start(): request._t=time.time()
@app.after_request
def _after(resp):
    try:
        dt=time.time()-getattr(request,"_t",time.time())
        REQ_LAT.labels(request.path,request.method).observe(dt)
        REQ_COUNT.labels(request.path,request.method,resp.status_code).inc()
    except: pass
    return resp

@app.get("/healthz")
@app.get("/api/healthz")
def healthz(): return {"status":"ok"},200

@app.get("/metrics")
def metrics(): return generate_latest(),200,{"Content-Type":CONTENT_TYPE_LATEST}

@app.get("/stations")
@app.get("/api/stations")
def stations():
    q=request.args.get("q")
    if not q: return jsonify(STATIONS)
    ql=q.lower(); return jsonify([s for s in STATIONS if ql in s["name"].lower()])

@app.get("/lines")
@app.get("/api/lines")
def lines(): return jsonify(LINES)

@app.get("/journey-mock")
@app.get("/api/journey-mock")
def journey():
    src=request.args.get("from"); dst=request.args.get("to")
    if not src or not dst: return {"error":"from and to are required"},400
    mid="Oxford Circus" if src!="Oxford Circus" and dst!="Oxford Circus" else "Green Park"
    return jsonify({"from":src,"to":dst,"stops":[src,mid,dst],"duration_min":10})

if __name__=="__main__": app.run(host="0.0.0.0",port=8000)
