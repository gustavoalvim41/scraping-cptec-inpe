import requests
from bs4 import BeautifulSoup

def main():
  url_base  = "http://servicos.cptec.inpe.br/XML/cidade/"
  url_suffix  = "/dia/0/ondas.xml"

  for id in range(1, 5565):
    response = requests.get(url_base + str(id) + url_suffix)
    soup = BeautifulSoup(response.content, "xml")
    name = soup.find("nome")
    uf = soup.find("uf")

    if name and name.text.strip() != "undefined":
      city_info = f"{id} - {name.text.strip()}, {uf.text.strip()}"
      print(city_info)
      
      with open("result.txt", "a", encoding="utf-8") as f:
        f.writelines(city_info + "\n")
        
    else:
      print(f"A cidade com o ID {id} não foi encontrada.")

if __name__ == "__main__":
  main()
  