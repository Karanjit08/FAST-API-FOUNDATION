from pydantic import BaseModel, Field


class PincodeRequest(BaseModel):
    pincode: str = Field(
        ...,
        min_length=6,
        max_length=6,
        pattern=r"^\d{6}$"
    )


class PinCodeResponse(BaseModel):
    pincode: str
    city: str
    state: str
    status: str   