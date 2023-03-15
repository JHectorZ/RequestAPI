#Aqui esta la clase que se utilizara como modulo para el manejo del JSON
from conn import GetAPI

class JsonManager():
    
    def __init__(self, jsonArray):
        self.jsonArray = jsonArray
        self.categoriesSet = {i['category']['name'] for i in self.jsonArray}
    
    
    #Este metodo es para poder ver una lista de todos los productos que hay en una lista
    def showProducts(self):
        print('\nEstos son los productos que tenemos nuestra tienda: \n')
        
        for item in self.jsonArray:
            print('[ ID: {:03d}                            Nombre: {} ] '.format(item['id'], item['title'].ljust(28, '_')))
            
    
    #Este metodo es para poder ver una lista de la categoria de productos que existen
    def showCategories(self):
        print('\nEstas son las categorias de la tienda: \n')
        
        for i, e in enumerate(self.categoriesSet):
            print(f'{i+1}.{e}')
            
            
    
    
# print('ID: {id}   Nombre: {name}    Precio: {price}    Categoria: {category}\n'
#       'Descripción: {description}')




if __name__ == '__main__':
    listaA = GetAPI()
    managed = JsonManager(listaA)
    
    managed.showCategories()