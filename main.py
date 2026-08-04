from fastapi import FastAPI


app = FastAPI(
    title= "CHAI POINT MENU API"
)


@app.get("/")
def root():
    return {"message": "Welcome to Chai Point Menu"}