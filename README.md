## html2ai2json 

Usually for web-scraping you have to manually identify the classes or "structure" of the webpage and then manually code the schema up in order to parse the page into a desired format. Why not let an LLM handle that problem for you? That was the guiding question for this project and just seeing how effective it was.

The key heuristic/insight here is that HTML itself is already a pretty structured language. It becomes even more structured when developers apply classes that are usually repeated when being used to display textual or quantitative information. So the foundation of converting HTML to JSON is seeing if there are repeated classes and only selecting those chunks to pass into the LLM.

An important disclaimer, I think especially when it comes to textual data, is that it's not performing any "coding" or "analysis" on the textual information, it is simply returning a programmatic interface, or in another words its just returning JSON. Sometimes it even just returns the HTML structure in JSON format if there weren't any specific classes that would give a valid result.

The end goal for all of this is that it's easier to load and work with JSON than HTML for analysis, at least for me.


## Installation

### Prerequisites

- Python
- Mistral Free (https://console.mistral.ai/home)
- Selenium WebDriver (https://googlechromelabs.github.io/chrome-for-testing/)

### Set-Up

1. Clone the repository:
```
git clone https://github.com/You-Gao/UVA-Event-Oracle.git
pip install -r requirements.txt
```

2. Modify Variables:
* Set the website you want to scrape in the notebook.
* Download the Selenium WebDriver and have the PATH env set correctly

## Usage (WIP)
With all said and done, the project should run correctly... *Fingers Crossed

## License
This project is licensed under the [Creative Commons CC0 1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/). See the [LICENSE](LICENSE) file for more details.

