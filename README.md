# TextAnalyzerService
Python Microservices App using FastAPI Framework

The Text Analysis Platform is a microservices architecture that provides a centralized system for managing and interacting with multiple text analysis services, including sentiment analysis, word count, and entity recognition.

## Key Features

- **Central Microservice:** Manages different text analysis services, allowing clients to interact with them through a single API endpoint.
- **Scalability:** Each text analysis service operates independently, enabling easy scaling and adding new services as needed.
- **Text Analysis Services:**
  - **Sentiment Analysis:** Analyzes the sentiment of the text (positive, neutral, negative).
  - **Word Count:** Counts the number of words in the text.
  - **Entity Recognition:** Identifies and classifies named entities (e.g., persons, organizations, locations) in the text.

## Environment Setup

1. Clone the repository: git clone https://github.com/your-username/textanalyzer.git 
2. Navigate to the project directory: cd PythonFast
3. Install dependencies:  pip install -r requirements.txt 


## Running the Microservice Architecture

1. Start the central microservice: uvicorn central_microservice.main:app --host 0.0.0.0 --port 8000
2. Start each text analysis service:
   
   - **Start Sentiment Analysis:** uvicorn sentiment_analysis_service.main:app --host 0.0.0.0 --port 8001
  - **Start Word Count:** uvicorn word_count_service.main:app --host 0.0.0.0 --port 8002
   - **Start Entity Recognition:** uvicorn entity_recognition_service.main:app --host 0.0.0.0 --port 8003

3. Use the central microservice endpoint (`http://localhost:8000/analyze`) to interact with the text analysis services.
   
## Available API Calls: 
Open Postman and send the appropriate Key:Value to test each api call. Make sure you are selecting correctly POST/GET/DELETE as indicated below.

1. POST -> https://localhost/800/textanalyzer =>

## Running Tests
Navigate to the directory containing the test folder and Run the following commands:

1. pytest PythonFast/tests/test_central_microservice.py
2. pytest PythonFast/tests/test_sentiment_analysis_service.py
3. pytest PythonFast/tests/test_word_count_service.py
4. pytest PythonFast/tests/test_entity_recognition_service.py
   




   

