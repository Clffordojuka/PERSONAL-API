from fastapi import FastAPI
from personal_api.routers import customer

app = FastAPI()

# Include the customer router
app.include_router(customer.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal API!"}