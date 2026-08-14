class PincodeNotFoundException(Exception):

    def __init__(self, pincode: str):
        self.pincode = pincode
        self.message = f"Pincode {pincode} was not found"

        super().__init__(self.message)


        