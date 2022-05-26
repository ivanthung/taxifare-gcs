from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hello from the Cloud Run"
