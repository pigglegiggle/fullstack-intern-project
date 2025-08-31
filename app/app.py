from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/ingest")
async def ingest(request: Request):
    data = await request.json()
    print("Received log:", data)
    return {"status": "ok"}
