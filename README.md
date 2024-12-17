## UVA Event Oracle (www.yougao.dev/UVA-Event-Oracle/)
This project is designed to scrape events from a list of UVA calendar sites within different departments and process them into a structured format (JSON or CSV). It utilizes '**requests**' and '**Selenium**' for web scraping, allowing for interaction with JavaScript-rendered content. 

The technical motivation of the project was wanting to use LLMs, specifically '**VertexAI**' (Google Cloud AI), to extract and create a JSON file from processed HTML files. However, what drove me was a more personal goal to explore what was going on around UVA and the different seminars that were being hosted.

This project would be completely useless if the departments all had g calendars set-up.

## Installation

### Prerequisites

- Python
- Google Cloud *Free Tier is Fine
- Google CLI (https://cloud.google.com/sdk/docs/install)
- Selenium WebDriver (https://googlechromelabs.github.io/chrome-for-testing/)

### Set-Up

1. Clone the repository:
```
git clone https://github.com/You-Gao/UVA-Event-Oracle.git
pip install -r requirements.txt
gcloud auth login
```

2. Modify Variables:
* In "scraping notebook.ipynb" replace project_id and location to match your Google Cloud Project
* Download the Selenium WebDriver and have the PATH env set correctly

## Usage (WIP)
With all said and done, the project should run correctly... *Fingers Crossed

## License
This project is licensed under the [Creative Commons CC0 1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/). See the [LICENSE](LICENSE) file for more details.

