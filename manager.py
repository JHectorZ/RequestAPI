#Aqui esta la clase que se utilizara como modulo para el manejo del JSON


class JsonManager():
    
    def __init__(self, jsonArray):
        self.jsonArray = jsonArray
        self.categoriesSet = {i['category']['name'] for i in self.jsonArray}
        self.categoriesJson = {category: list(filter(lambda x: category == x['category']['name'], self.jsonArray))
                               for category in self.categoriesSet}
    
    
    def __str__(self) -> str:
        return "JsonManager"
    
    
    #Este metodo es para poder ver una lista de todos los productos que hay en una lista
    def showProducts(self):
        print('\nEstos son los productos que tenemos nuestra tienda: \n')
        
        for item in self.jsonArray:
            print('[ ID: {:03d}                            Nombre: {} ] '
                  .format(item['id'], item['title'].ljust(28, '_')))
            
    
    #Este metodo es para poder ver una lista de la categoria de productos que existen
    def showCategories(self):
        print('\nEstas son las categorias de la tienda: \n')
        
        for i, e in enumerate(self.categoriesSet):
            print(f'{i+1}.{e}')
        
            
    #En este metodo sirve para poder filtar los productos mediante sus categorias           
    def filterCategories(self):
        self.showCategories()
        categoryFilter = input('\nDigite el numero de la categoria que deseas filtrar: ').capitalize()
        
        print()
        for product in self.categoriesJson[categoryFilter]:
            print('[ {} ]'.format(product['title'].ljust(28, '_')))
    
    
    #Este metodo sirve para que puedas ver un solo producto por completo
    def showOneProduct(self):
        productFilter = input('\nDigite el producto que deseas filtrar: ').title()
        productSearch = list(filter(lambda x: productFilter == x['title'], self.jsonArray))
        dic = productSearch[0]
        print('ID: {}   Nombre: {}    Precio: {}    Categoria: {}\n'
            'Descripción: {}'.format(dic['id'], dic['title'], dic['price'], dic['category']['name'], dic['description']))



if __name__ == '__main__':
    from conn import GetAPI
    
    array = GetAPI()
    managed = JsonManager(array)
