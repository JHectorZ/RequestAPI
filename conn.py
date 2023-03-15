#Se importa el modulo requerido para hacer el request del API
import requests


#Se crea una funcion para obtener los datos del request
def GetAPI():
    data = requests.get('https://api.escuelajs.co/api/v1/products')
    
    if data.status_code != 200:
        return Exception('Hubo un error en request')
    
    return data.json()
    

#Aqui hacemos el llamado de la funcion para que nos regrese un JSON
#Si hay un error en la peticion regresara un error

try:
    dataJson = GetAPI()
except Exception as error:
    print(error)


if __name__ == '__main__':
    setJson = {i['category']['name'] for i in dataJson}
    print(setJson)