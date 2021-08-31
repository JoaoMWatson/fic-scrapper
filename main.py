import requests
from rich.console import Console
from bs4 import BeautifulSoup

# 2 -> 126
BASE_URL = 'https://exiledrebelsscanlations.com/'
console = Console()

def set_text():
    text_content = ""
    for p in range(2, 126):
        try:
            if p == 74:
                pass
            else:
                html_doc = requests.get(BASE_URL + 'gdc-chapter-'+str(p)+'/').content
                soup = BeautifulSoup(html_doc, 'html.parser')

                content = soup.find(id='wtr-content')
                title = soup.find('h1', class_="entry-title")
                paragraphs = content.find_all('p')

                console.log(f"Chapter: {p} contains {paragraphs.__len__()} paragraphs :D")

                text_content += f"\n{' '*30}*{title.text}*\n{'='*70}\n"
                for i in paragraphs:
                    text_content += i.text + "\n"+"\n"
        except Exception:
            pass
    return text_content


def write_in_doc(content):
    with open('content.txt', 'w') as f:
        f.write(content)
    print("Done!")


if __name__ == '__main__':
    content = set_text()
    write_in_doc(content)
