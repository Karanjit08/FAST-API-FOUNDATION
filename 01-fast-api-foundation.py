from fastapi import FastAPI


app = FastAPI(
    title="Swiggy Order Service",
    description=(
        "Internal API for managing orders"
        "Serving Customers always"
    ),
    version="1.2.3",
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
            "region": "ap-south-2",
            "version": "1.2.3"
            }

@app.get("/orders")
def get_orders():
    """RETURNS ORDERS DATA"""
    return [
        {"id": 1, "item": "Butter Chicken"},
        {"id": 2, "item": "Masala Dosa"},
        {"id": 3, "item": "Paneer Tikka"},
    ]