import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional
from urllib.parse import urljoin
from open_api import open_api_call

class WebScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        # Add common headers to mimic a real browser
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def get_page_content(self, url: str) -> BeautifulSoup:
        """
        Fetch and parse a web page.
        
        Args:
            url: The URL to fetch
            
        Returns:
            BeautifulSoup object of the parsed page
        """
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'lxml')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            raise

    def extract_text_content(self, url: str) -> Dict[str, str]:
        """
        Extract main text content from a webpage.
        
        Returns:
            Dictionary containing title and main content
        """
        soup = self.get_page_content(url)
        
        # Get title
        title = soup.title.string if soup.title else "No title found"
        
        # Get main content (adjust selectors based on the website structure)
        main_content = []
        
        # Try to find main content area
        content_areas = soup.find_all(['article', 'main', 'div'], class_=['content', 'main-content', 'article'])
        if content_areas:
            for area in content_areas:
                paragraphs = area.find_all('p')
                main_content.extend(p.get_text().strip() for p in paragraphs if p.get_text().strip())
        else:
            # Fallback to all paragraphs if no main content area found
            paragraphs = soup.find_all('p')
            main_content.extend(p.get_text().strip() for p in paragraphs if p.get_text().strip())

        return {
            "title": title,
            "content": "\n\n".join(main_content)
        }

    def extract_links(self, url: str) -> List[Dict[str, str]]:
        """
        Extract all links from a webpage.
        
        Returns:
            List of dictionaries containing link text and URL
        """
        soup = self.get_page_content(url)
        links = []
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Convert relative URLs to absolute URLs
            if not href.startswith(('http://', 'https://')):
                href = urljoin(self.base_url, href)
            
            links.append({
                "text": link.get_text().strip(),
                "url": href
            })
        
        return links

    def extract_images(self, url: str) -> List[Dict[str, str]]:
        """
        Extract all images from a webpage.
        
        Returns:
            List of dictionaries containing image alt text and URL
        """
        soup = self.get_page_content(url)
        images = []
        
        for img in soup.find_all('img', src=True):
            src = img['src']
            if not src.startswith(('http://', 'https://')):
                src = urljoin(self.base_url, src)
            
            images.append({
                "alt": img.get('alt', ''),
                "url": src
            })
        
        return images

    def extract_tables(self, url: str) -> List[List[List[str]]]:
        """
        Extract all tables from a webpage.
        
        Returns:
            List of tables, where each table is a list of rows
        """
        soup = self.get_page_content(url)
        tables = []
        
        for table in soup.find_all('table'):
            current_table = []
            rows = table.find_all('tr')
            
            for row in rows:
                # Get cells (both header and data cells)
                cells = row.find_all(['td', 'th'])
                current_row = [cell.get_text().strip() for cell in cells]
                if current_row:  # Only add non-empty rows
                    current_table.append(current_row)
            
            if current_table:  # Only add non-empty tables
                tables.append(current_table)
        
        return tables


# Example usage
if __name__ == "__main__":
    # Example URL - replace with your target website
    target_url = "https://en.wikipedia.org/wiki/New_York_City"
    scraper = WebScraper(target_url)
    
    try:
        # Extract text content
        content = scraper.extract_text_content(target_url)
        facts=open_api_call(content['content'])
        print(facts)
        
    except Exception as e:
        print(f"Error during scraping: {e}")