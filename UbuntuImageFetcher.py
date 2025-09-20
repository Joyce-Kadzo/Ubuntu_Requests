import os
import requests
from urllib.parse import urlparse
import uuid
import hashlib

# Configuration
ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/gif"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB limit

def get_file_hash(content):
    """Generate a hash for the file content to detect duplicates."""
    return hashlib.md5(content).hexdigest()

def fetch_images(urls):
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    downloaded_hashes = set()

    for url in urls:
        url = url.strip()
        if not url:
            continue

        try:
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()

            # Check headers
            content_type = response.headers.get("Content-Type", "")
            if content_type not in ALLOWED_MIME_TYPES:
                print(f"Skipped {url} - Unsupported content type: {content_type}")
                continue

            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > MAX_FILE_SIZE:
                print(f"Skipped {url} - File too large ({int(content_length) / (1024*1024):.2f} MB)")
                continue

            # Read content safely
            content = response.content

            # Check for duplicates
            file_hash = get_file_hash(content)
            if file_hash in downloaded_hashes:
                print(f"Skipped {url} - Duplicate image detected")
                continue
            downloaded_hashes.add(file_hash)

            # Extract or generate filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = f"image_{uuid.uuid4().hex}.jpg"

            file_path = os.path.join(folder_name, filename)

            # Save file
            with open(file_path, "wb") as f:
                f.write(content)

            print(f"Downloaded and saved: {file_path}")

        except requests.exceptions.MissingSchema:
            print(f"Invalid URL: {url}. Please include 'http://' or 'https://'.")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error for {url}: {e}")
        except requests.exceptions.ConnectionError:
            print(f"Connection error for {url}.")
        except requests.exceptions.Timeout:
            print(f"Request timed out for {url}.")
        except Exception as e:
            print(f"Unexpected error for {url}: {e}")

if __name__ == "__main__":
    print("Enter image URLs (separated by spaces):")
    urls = input().split()
    fetch_images(urls)
