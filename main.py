from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Sample API",
    description="A minimal FastAPI app with automatic Swagger UI documentation.",
    version="1.0.0"
)

@app.get("/health", summary="Health Check", description="Returns service health status.")
async def health_check():
    """Simple health check endpoint returning status OK."""
    return {"status": "ok"}
