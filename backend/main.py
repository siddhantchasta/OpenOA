from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pkgutil
import openoa

app = FastAPI(title="OpenOA Backend Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "OpenOA backend running successfully"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"openoa_version": getattr(openoa, "__version__", "unknown")}

@app.get("/modules")
def list_modules():
    modules = [m.name for m in pkgutil.iter_modules(openoa.__path__)]
    return {"available_modules": modules}
