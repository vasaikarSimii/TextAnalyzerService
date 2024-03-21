# word_count_service/main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging

app = FastAPI()


@app.post("/word_count")
def count_words(text: str):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Received request, the text is ",text)
    words = text.split()
    return JSONResponse(content={"word_count": len(words)})

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)