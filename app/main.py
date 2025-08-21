from fastapi import FastAPI
from manager import AppManager

app = FastAPI(title="Hostile Tweets Processor")
manager = AppManager()

@app.get("/tweets")
def get_tweets():
    return manager.run_pipeline()