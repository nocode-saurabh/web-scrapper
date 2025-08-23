# Web Scraper API

A FastAPI-based web scraping service with basic health check endpoint.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Run the application using:
```bash
python main.py
```

The server will start at `http://localhost:8000`

## Available Endpoints

### Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Response**: 
```json
{
    "status": "healthy",
    "version": "1.0.0"
}
```

## API Documentation
Once the server is running, you can access:
- Swagger UI documentation at: `http://localhost:8000/docs`
- ReDoc documentation at: `http://localhost:8000/redoc`