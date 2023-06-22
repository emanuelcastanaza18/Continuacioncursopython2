
#Se pueden usar los metodos de: get (Listar), post (Crear), put/patch (actualizar), delete (eliminar)
#https://jsonplaceholder.typicode.com/users
# import requests


# url = "https://jsonplaceholder.typicode.com/users"

# r = requests.get(url, timeout=10)
# # print(r)
# # print(r.status_code) #Para saber el estado
# # #Para saber el resultado del llamado 
# # print(r.text)
# #Para saber el resutaldo en formato json
# r = r.json()

# for user in r:
#     print(user['name'])

#Para obtener un usuario en particular
# import requests
# 
# url = "https://jsonplaceholder.typicode.com/users/"
# 
# r = requests.get(url, timeout=10)
# r = r.json()
#  
# url = "https://jsonplaceholder.typicode.com/users/1"
# 
# r = requests.get(url, timeout=10)
# print(r.json())


#Para buscar un recurso
# import requests

# url = "https://jsonplaceholder.typicode.com/users/"
# user = {
#     "name": "Chanchito Feliz",
# }
# r = requests.post(url, timeout=10, data=user)
# print(r.status_code)


#Para put y patch
# import requests

# url = "https://jsonplaceholder.typicode.com/users/2"
# user = {
#     "name": "Chanchito Feliz",
# }
# r = requests.put(url, timeout=10, data=user)
# print(r.status_code)

#Para eliminar
# import requests

# url = "https://jsonplaceholder.typicode.com/users/2"

# r = requests.delete(url, timeout=10)
# print(r.status_code)

#200 Para listar
#201 Para crear
#204 Para actualizar o eliminar


#headers
import requests

url = "https://jsonplaceholder.typicode.com/users/2"
apikey = "123456"
headers = {
    "Authorization": f"Bearer {apikey}"
}
r = requests.delete(url, timeout=10, headers=headers)
print(r.status_code)

