# main.py

from fastapi import FastAPI

# Create a FastAPI "instance"
# This 'app' variable will be the main point of interaction to create your API.
app = FastAPI()

# Define a "path operation decorator"
# @app.get("/") tells FastAPI that the function below it handles
# HTTP GET requests to the root path ("/") of your API.
@app.get("/")
# Define the "path operation function"
# This is an asynchronous function (async def) because FastAPI is built for async.
# It will be called when a request hits the "/" path with a GET method.
async def read_root():
    # Return a Python dictionary, which FastAPI will automatically
    # convert into a JSON response.
    return {"message": "Hello, World!"}