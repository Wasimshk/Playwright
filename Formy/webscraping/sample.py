import requests
from bs4 import BeautifulSoup

response = requests.get("https://formy-project.herokuapp.com")
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

soup = BeautifulSoup(html_content, "html.parser")
links = soup.find_all("a")


arr = []
for link in links:
    arr.append(link.get_text(strip=True)) # strip=True removes extra spaces/newlines, and filters only the texts of the element

print(len(arr))
