# TextAnalyzerService
Python Microservices App using FastAPI Framework

The Text Analysis Platform is a microservices architecture that provides a centralized system for managing and interacting with multiple text analysis services, including sentiment analysis, word count, and entity recognition. The app uses Object-Oriented Programming principles as well as best practices to write clean code utilizing functions, classes, and modules as needed. All user requests are hitting one single API : /textanalyzer which then reroutes each request to the right port and service based on the service_name mentioned in the input parameter.

## Microservices Design
![MicroServices Design](https://github.com/vasaikarSimii/TextAnalyzerService/assets/71291381/3162c76f-f6fa-40df-84ee-4dfc8e16c2d1)


## Key Features

- **Central Microservice:** Manages different text analysis services, allowing clients to interact with them through a single API endpoint.
- **Scalability:** Each text analysis service operates independently, enabling easy scaling and adding new services as needed.
- **Text Analysis Services:**
  - **Sentiment Analysis:** Analyzes the sentiment of the text (positive, neutral, negative).
  - **Word Count:** Counts the number of words in the text.
  - **Entity Recognition:** Identifies and classifies named entities (e.g., persons, organizations, locations) in the text.

## Environment Setup

1. Clone the repository: git clone git@github.com:{your-username}/TextAnalyzerService.git
2. Navigate to the project directory: cd PythonFast
3. Install dependencies:  pip install -r requirements.txt 


## Running the Microservice Architecture

1. Start the central microservice: uvicorn central_microservice.main:app --host 0.0.0.0 --port 8000
2. Start each text analysis service in separate bash terminals:
   
   - **Start Sentiment Analysis:** uvicorn sentiment_analysis_service.main:app --host 0.0.0.0 --port 8001
  - **Start Word Count:** uvicorn word_count_service.main:app --host 0.0.0.0 --port 8002
   - **Start Entity Recognition:** uvicorn entity_recognition_service.main:app --host 0.0.0.0 --port 8003

3. Use the central microservice endpoint (`http://localhost:8000/textanalyzer`) to interact with the text analysis services.
   
## Available API Calls: 
Use Postman to test APIs and send the appropriate Key: Value as Query Params for each call. Make sure you are selecting correctly POST/GET/DELETE as indicated below.

1. - **Register Service:**:  POST -> http://localhost/8000/resgister => Input params= {"service_name": "word_count", "port": "8002"}
2. - **List Services:**:  GET -> http://localhost:8000/services
3. - **Remove Services:**: DELETE -> http://localhost:8000/remove_service => Input params= {"service_name": "word_count"}
4. - **Sentiment Analysis Service:**:  POST -> http://localhost/8000/textanalyzer => Input params= {"service_name": "sentiment_analysis", "text": "Today is a Good Day"}
5. - **Word Count Service:**:  POST -> http://localhost/8000/textanalyzer => Input params= {"service_name": "word_count", "text": "Today is a Good Day"}
6. - **Entity Recognition Service:**:  POST -> http://localhost/8000/textanalyzer => Input params= {"service_name": "entity_recognition", "text": "Today is a Good Day"}

## Running Tests
Navigate to the directory containing the test folder and Run the following commands. Make sure all microservices are up and running before running test:

1. pytest tests/test_central_microservice.py
2. pytest tests/test_sentiment_analysis_service.py
3. pytest tests/test_word_count_service.py
4. pytest tests/test_entity_recognition_service.py
   




   

