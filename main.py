from fastapi import FastAPI
import random

app = FastAPI()

health_states = {}

@app.get("/")
def root():
    return {"service": "anomiq-verification-simulator"}


@app.get("/verify/resource/{ci_id}")
def verify_resource(ci_id: str):

    state = health_states.get(ci_id)

    if not state:
        state = random.choice(["healthy", "degraded", "failed"])
        health_states[ci_id] = state

    return {
        "ci_id": ci_id,
        "health": state,
        "confidence": round(random.uniform(0.7, 0.98),2)
    }


@app.post("/set-health")
def set_health(payload: dict):

    ci = payload["ci_id"]
    state = payload["health"]

    health_states[ci] = state

    return {"ci_id": ci, "health": state}