import requests
from bs4 import BeautifulSoup
url = "https://www.geeksforgeeks.org/basics-computer-networking/"
res = requests.get(url)


if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    
    #div class = "text"
    section_to_ignore = soup.find("div", class_="article_bottom_text")
    if section_to_ignore:
        section_to_ignore.extract()
    text = soup.find('div', class_ = "text").get_text(separator="\n", strip=".")
    print(text)
    text_data = "\n".join([t.get_text() for t in soup.find_all('div', class_ = "text")])
    with open("scraped_text_data.txt", "w", encoding="utf-8") as file:
        file.write(text_data)
    
    #p tag
    # text_data = "\n".join([p.get_text() for p in soup.find_all("p")])
    # with open("scraped_p_data.txt", "w", encoding="utf-8") as file:
    #     file.write(text_data)
    print("Data has been scraped and saved to scraped_data.txt.")
else:
    print("Failed to retrieve the web page.")