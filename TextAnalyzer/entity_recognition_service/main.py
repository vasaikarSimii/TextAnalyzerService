from fastapi import FastAPI, HTTPException
from spacy import load
from pydantic import BaseModel
import logging

app = FastAPI()

nlp = load("en_core_web_sm")



class EntityRecognitionResponse(BaseModel):
    entities: list


@app.post("/entity_recognition", response_model=EntityRecognitionResponse)
def recognize_entities(text: str):
    logging.basicConfig(level=logging.DEBUG)
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    logging.debug("Received request, registered Service",text,doc,entities)
    return {"entities": entities}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8003)