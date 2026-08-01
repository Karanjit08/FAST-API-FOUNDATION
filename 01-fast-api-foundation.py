from fastapi import FastAPI


app = FastAPI(
    title="Swiggy Order Service",
    description=(
        "Internal API for managing orders"
        "Serving Customers always"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """END POINT - HEALTH CHECK"""
    return {"message": "Welcome to Swiggy Order Service", "status": "healthy"}


@app.get("/about")
def about():
    """RETURNS META DATA"""
    return {"service": "Order Service", 
            "team": "backend-platform",
            "region": "ap-south-1",
            "version": "1.2.2"
            }