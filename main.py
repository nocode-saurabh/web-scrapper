from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from scrapper import WebScraper
from open_api import open_api_call
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Web Scraper API",
    description="A web scraping API service",
    version="1.0.0"
)
app.add_middleware(
       CORSMiddleware,
       allow_origins=["https://nocode-saurabh.github.io/factopedia-web", "http://localhost:3000"],  # React app's origin
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
)

class HealthResponse(BaseModel):
    status: str
    version: str

@app.get("/health", response_model=HealthResponse)
async def health_check() -> Dict:
    """
    Health check endpoint to verify the API is running
    """
    return {
        "status": "healthy",
        "version": "1.0.0"
    }

class ScrapeRequest(BaseModel):
    url: str

class ScrapeResponse(BaseModel):
    title: str
    facts: str

@app.post("/scrape", response_model=ScrapeResponse)
async def scrape_url(request: ScrapeRequest) -> ScrapeResponse:
    """
    Scrape the given URL and return extracted facts.
    """
    scraper = WebScraper(request.url)
    content = scraper.extract_text_content(request.url)
    facts = open_api_call(content['content'])
    return ScrapeResponse(title=content['title'], facts=facts)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 4000))
    uvicorn.run(app, host="0.0.0.0", port=port)
