#https://stackoverflow.com/questions/
# import requests
# from bs4 import BeautifulSoup

# url = "https://stackoverflow.com/questions/"
# respuesta = requests.get(url)
# texto = respuesta.text
# soup = BeautifulSoup(texto, "html.parser")

# preguntas = soup.select(".s-post-summary")
# # print(preguntas[0])
# for pregunta in preguntas:
#     titulo = pregunta.select_one(".s-link").getText()
#     # print(titulo)
#     #Para obtener el nombre de los usuarios
#     usuario = pregunta.select_one(".s-user-card--link").getText()
#     print(f"{usuario.strip()} - Titulo: \n{titulo.strip()}")
    
#Para navegar a la pagina siguiente
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/"
respuesta = requests.get(url)
texto = respuesta.text
soup = BeautifulSoup(texto, "html.parser")

preguntas = soup.select(".s-post-summary")
print(preguntas[0]["data-post-id"])
for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").getText()
    usuario = pregunta.select_one(".s-user-card--link").getText()
    # print(f"{usuario.strip()} - Titulo: \n{titulo.strip()}")
