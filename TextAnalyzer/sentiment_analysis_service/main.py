
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from textblob import TextBlob
import logging

app = FastAPI()

@app.post("/sentiment_analysis")
def analyze_sentiment(text: str):
    # Configure logging to display debug messages
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Received request, registered Service",text)
    blob = TextBlob(text)
    sentiment = blob.sentiment
    if sentiment.polarity > 0:
        return JSONResponse(content={"sentiment": "positive"})
    elif sentiment.polarity == 0:
        return JSONResponse(content={"sentiment": "neutral"})
    else:
        return JSONResponse(content={"sentiment": "negative"})
    
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)