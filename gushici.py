import requests
import re

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
    "Refer":"https://www.gushiwen.org/",
}

def parse_url(url):
    response = requests.get(url,headers=headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,  re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        x = re.sub(r'<.*?>',"",content)
        contents.append(x.strip())
    poems =[]
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content,
        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        print("*"*30)

def main():
    for x in range(1,100):
        url = "https://www.gushiwen.org/default_{}.aspx".format(x)
        print(url)
        parse_url(url)


if __name__ == '__main__':
    main()