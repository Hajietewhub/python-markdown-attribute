# Article Markdown
A Node.js library to process markdown files using Python.

## Installation
npm install article-markdown

## Usage
After installation, run the following commands in your terminal:

### Process Images
article-markdown 1 <directory> [lineNumber] [urlTemplate]
Example:
article-markdown 1 ./my_folder 5 "https://example.com/image-{number}.jpg"

### Process Dates
article-markdown 2 <directory> [lineNumber] [date]
Example:
article-markdown 2 ./my_folder 2 2025-04-01

## Prerequisites
- Python 3.x must be installed and available in your system PATH.