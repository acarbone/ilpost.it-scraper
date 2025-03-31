# Il Post Scraper

A Python script that scrapes the latest news from Il Post and allows you to open them in your browser or generate summaries using Ollama.

## Features

- Fetches the latest 5 news articles from Il Post
- Fetches the latest 5 articles from the main content section
- Displays articles in a nicely formatted CLI table
- Allows opening articles in your default browser
- Generates article summaries using Ollama
- Clean and modular code structure following SOLID principles

## Requirements

- Python 3.6 or higher
- pip (Python package manager)
- Ollama installed and running on your system

## Installation

1. Clone this repository
2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with:
```bash
python ilpost_scraper.py
```

The script will display two tables:
1. "Last 5 news from Il Post" with the latest news
2. "Last 5 articles from Il Post" with the latest articles from the main content section

You can interact with the articles in two ways:
1. Enter the article number to open it in your default browser
2. Enter 's:number' to generate a summary of the article using Ollama (e.g., 's:1' for the first article)

To quit the program, enter 'q' when prompted.

## Project Structure

```
ilpost-scraper/
├── src/
│   ├── __init__.py
│   ├── models.py      # Data models
│   ├── fetcher.py     # Web page fetching
│   ├── parser.py      # HTML parsing
│   ├── display.py     # CLI display
│   ├── browser.py     # Browser interaction
│   ├── summarizer.py  # Article summarization
│   └── scraper.py     # Main scraper logic
├── ilpost_scraper.py  # Entry point
└── requirements.txt   # Dependencies
```

## Notes

- The script uses the `rich` library for beautiful CLI formatting
- Links are clickable directly in the terminal (if supported)
- Network errors are handled gracefully with appropriate error messages
- The code follows the Single Responsibility Principle for better maintainability
- Article summaries are generated using Ollama with the llama3.2:3b model
