# Image Downloader

A Python script for downloading images from URLs with duplicate detection, file type validation, and size restrictions.

## Features

- Downloads multiple images from provided URLs
- Validates image MIME types (JPEG, PNG, GIF)
- Enforces maximum file size limit (10MB)
- Detects and skips duplicate images using MD5 hashing
- Handles various HTTP errors and connection issues
- Generates unique filenames for images without proper extensions
- Organizes downloaded images in a dedicated folder

## Requirements

- Python 3.x
- requests library

## Installation

1. Clone or download this script
2. Install the required dependencies:

```bash
pip install requests
```

## Usage

1. Run the script:
```bash
python image_downloader.py
```

2. Enter image URLs separated by spaces when prompted:
```
Enter image URLs (separated by spaces):
https://example.com/image1.jpg https://example.com/image2.png
```

3. The script will download valid images to a folder named "Fetched_Images"

## Configuration

You can modify the following constants in the script:

- `ALLOWED_MIME_TYPES`: Set of allowed MIME types (default: image/jpeg, image/png, image/gif)
- `MAX_FILE_SIZE`: Maximum file size in bytes (default: 10MB)

## Error Handling

The script handles various error conditions:
- Invalid URLs (missing http/https prefix)
- HTTP errors (404, 403, etc.)
- Connection errors and timeouts
- Unsupported file types
- Files exceeding size limits
- Duplicate images

## Output

All downloaded images are saved in the "Fetched_Images" directory with:
- Their original filename if available, or
- A generated UUID-based filename if the URL doesn't contain one

## Notes

- The script uses MD5 hashing for duplicate detection
- All images are stored in memory during processing
- The script creates the output directory if it doesn't exist

