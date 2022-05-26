from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "I updated myself with Continuous Deployment in the Cloud Run"
