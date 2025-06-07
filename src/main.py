from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/")
async def get_root() -> FileResponse:
    return FileResponse("static/index.html")
