from fastapi import FastAPI, Request
from models.pincodes import PincodeRequest, PinCodeResponse
import json
from exceptions.exceptions import PincodeNotFoundException
from fastapi.responses import JSONResponse

app = FastAPI( 
    title="PinCode Lookup",
    description="API to find city and state using an Indian Pincode",
    version="1.0.0"
    )

@app.exception_handler(PincodeNotFoundException)
async def pincode_not_found_exception_handler(
    request: Request,
    exc: PincodeNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "PincodeNotFound",
            "message": exc.message
        }
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to PinCode Lookup", "status": "Active"}

@app.post("/pincode")
def lookup_pincode(request: PincodeRequest):

    with open("data/pincodes.json", "r") as file:
        pincodes = json.load(file)

    for pincode_data in pincodes:

        if pincode_data["pincode"] == request.pincode:
            return PinCodeResponse(
                pincode= pincode_data["pincode"],
                city=pincode_data["city"],
                state=pincode_data["state"],
                status="OK"
            )

    raise PincodeNotFoundException(request.pincode)