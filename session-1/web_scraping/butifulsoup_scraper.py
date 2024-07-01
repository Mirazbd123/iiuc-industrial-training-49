from bs4 import BeautifulSoup
import requests

def get_ex(url):
    res = requests.get(url)
    headers = {
         'User-Agent': 'My User Agent 1.0',
         'Accept': 'application/json' 
         }
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.text

def main():
    url = 'https://www.prothomalo.com/politics/ebs6a4ycqz'
    print(get_ex(url))


if __name__ == "__main__":
    main()