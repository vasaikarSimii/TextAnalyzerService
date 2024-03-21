from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import logging
import requests


# Configure logging to display debug messages
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

services = {}


class ServiceInfo(BaseModel):
    name: str
    url: str


@app.post("/register")
def register_service(service_name: str, port: int):
    services[service_name] = f"http://localhost:{port}/{service_name}"
    logging.debug("Received request, registered Service",service_name )
    return {"message": f"Voila! Service Registered Successfully {service_name}"}



@app.get("/services", response_model=List[ServiceInfo])
def get_services():
    logging.debug("Received request, registered Service",services)
    return [{"name": name, "url": url} for name, url in services.items()]
    
@app.delete("/remove_service")
def remove_service(service_name: str):
    if service_name not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    del services[service_name]
    return {"message": f"Service '{service_name}' removed successfully."}


@app.post("/textanalyzer")
def analyze_text(service_name: str, text: str):
    service_url = services.get(service_name)
    if not service_url:
        raise HTTPException(status_code=404, detail="Service not found")
    logging.debug("Received request, registered Service",service_name,service_url,text)
    response = requests.post(service_url, params={"text": text})
    logging.debug("resposne  = ",response)
    return response.json()
