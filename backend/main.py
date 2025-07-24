import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from database import SessionLocal, engine
from models import Base
from routers import incident_router, resource_router, communication_router  # Add more routers as needed

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
origins = ["*"]  # Replace with your allowed origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

# Dependency injection for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register routers
app.include_router(incident_router.router)
app.include_router(resource_router.router)
app.include_router(communication_router.router) # Add more routers as needed

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Error handling
@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": str(exc)})

# Static file serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    templates = Jinja2Templates(directory="static")

    @app.get("/{file_path:path}")
    async def serve_frontend(file_path: str, request: Request):
        if file_path.startswith("api"):
            return None
        html_file = os.path.join("static", file_path)
        if os.path.isfile(html_file):
            return FileResponse(html_file)
        return templates.TemplateResponse("index.html", {"request": request})

# OpenAPI documentation
app.openapi_url = "/openapi.json"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
