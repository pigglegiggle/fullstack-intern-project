from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"

@app.post("/ingest")
async def ingest(request: Request):
    data = await request.json()
    print("Received log:", data)
    return {"status": "ok"}
