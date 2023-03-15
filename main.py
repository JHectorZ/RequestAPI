#Importamos los archivos para usarlos como moduladores
from manager import JsonManager
from conn import GetAPI


#Hacemos el request del API 
try:
    dataJson = GetAPI()
except Exception as error:
    print(error)



#Creamos el objeto para manejar el Json
manJson = JsonManager(dataJson)


#Hacemos la la interface del usuario
print('\nMenu de manejo de la fakeStore de API')
answer = int(input('\n1.Mostrar todos los productos\n2.Mostrar todas las categorias\n3.Filtrar por categorias\n4.Mostrar un producto\n'
                   '\nDigite su respuesta: '))


if answer == 1:
    manJson.showProducts()
    
elif answer == 2:
    manJson.showCategories()
    
elif answer == 3:
    manJson.filterCategories()
    
elif answer == 4:
    manJson.showOneProduct()

else:
    print('Ha ocurrido un error')



