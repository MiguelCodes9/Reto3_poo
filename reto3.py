##reto 3
#esta es la clase padre de la cual heredan las demas clases
class MenuItem():
    def __init__(self,name, price): #atributos de la clase que es nombre y precio
        self.name=name
        self.price=price
    def total_price(self): #este metodo solo devuelve el precio del item, ya que preferi definir el precio al crear el objeto
        return self.price
    #Este atributo sirve para facilitar la impresion de los objetos, 
    def __str__(self): #De aqui hacia abjajo todas las clases tienen este metodo menos order
        return f"{self.name} - ${self.price}"  
    #clase para el plato de entrada
class StartDish(MenuItem):
    def __init__(self, name, price, type):
        super().__init__(name,price)
        self.type=type
    def __str__(self):
        return f"{self.name}, tipo {self.type} - ${self.price}"
    #clase para el plato fuerte
class MainDish(MenuItem):
    def __init__(self, name, price):
        super().__init__(name,price)
    def __str__(self):
        return f"{self.name} - ${self.price}"
    #clase para la bebida
class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name,price)
        self.size=size
    def __str__(self):
        return f"{self.name}, tamaño {self.size} - ${self.price}"
    #clase para el postre
class Dessert(MenuItem):
    def __init__(self, name, price, flavor):
        super().__init__(name,price)
        self.flavor=flavor
    def __str__(self):
        return f"{self.name}, textura {self.flavor} - ${self.price}"

class order():#Esta clase recibe los cuatro objetos que componen la orden
    def __init__(self,startdish,maindish,beverage,dessert):
        self.startdish=startdish
        self.maindish=maindish
        self.beverage=beverage
        self.dessert=dessert
        #esta funcion accede a los precios de cada objeto y los suma
    def total_order(self):
        price=(
            self.startdish.total_price()+
            self.maindish.total_price()+
            self.beverage.total_price()+
            self.dessert.total_price()
        )
        #el descuento es del 15% si la compra es mayor a 50000
        descuento=15
        if price>50000:
            price=price-(price*descuento/100)
            return (price, "aplico un descuento del 15% por compras mayores a $50000")
        else:
         return price 
    #esta funcion imprime la orden de una manera mas amigable
    def show_order(self):
        print("Tu orden es la siguiente:")
        #se le asigan a variables los precios y nombres de cada objeto para facilitar la impresion
        p_entrada=self.startdish.price  
        p_fuerte=self.maindish.price 
        p_bebidas=self.beverage.price 
        p_postres=self.dessert.price 
        entrada=self.startdish.name
        plato_fuerte=self.maindish.name
        bebida=self.beverage.name
        postre=self.dessert.name
        #se imprimen los resultados
        print("Plato de entrada:       ", entrada,   "--$", p_entrada)
        print("Plato fuerte:           ", plato_fuerte, "--$",p_fuerte)
        print("Bebida:                 ", bebida,  "--$",p_bebidas)
        print("Postre:                 ", postre, "--$",p_postres)
        print("El total a pagar es:   $", self.total_order())

## Aqui estan conteniadas las opciones que el usuario puede escoger
entradas=[
    StartDish("Empanada de carne", 3000, "frito"),
    StartDish("Empanada campesina", 3200, "frito"),
    StartDish("Sopa de tomate", 6000, "caliente"),
    StartDish("Patacon con ahogao", 3000, "frito"),
]
PlatosFuertes=[
    MainDish("Bandeja Paisa", 37000),
    MainDish("Cocido boyacense", 30200),
    MainDish("Ajiaco", 26000 ),
    MainDish("Tamal", 12000),
    MainDish("Chuleta de cerdo", 21000),
    MainDish("Costillas BBQ", 25000),
    MainDish("Baby Beef", 32000),
    MainDish("Arroz con pollo", 10000),
    MainDish("Lechona", 12000),
    MainDish("Frijolada", 17000),
    MainDish("Sancocho", 14000),
    MainDish("Sudado de pollo", 11000)  
   
] 

bebidas = [
    Beverage("Jugo de mango", 3000 , "grande"),
    Beverage("Jugo de mora", 2500 , "mediana"),
    Beverage("Jugo de maracuya", 3000, "grande"),
    Beverage("Cocacola", 5500 , "1.5 L"),
    Beverage("Cocacola personal", 3000, "grande"),
    Beverage("Pepsi personal", 2500 , "Pequeña"),
    Beverage("Te", 2000, "Pequeño"),
    Beverage("Cerveza", 2800, "mediana"),
]

postres = [
    Dessert("Helado de brownie", 2500, "esponjosa"),
    Dessert("Helado de vainilla", 2500, "cremoso"),
    Dessert("Flan de caramelo", 3000, "gelatinoso"),
    Dessert("Cheesecake de mora", 4500, "gelatinoso"),
    Dessert("Arroz con leche", 3000, "espeso")
]
#esta funcion muestra las opciones de cada categoria
def mostrar_opciones(list, title):
     print(f"  --- {title} ---")
     for i, item in enumerate(list, 1): #  enumerate permite obtener el indice y el item en cada iteracion 
        print(i, item)
     print("---------------------------")
#Esta funcion es importante ya que permite al usuario seleccionar una opcion y valida que la opcion sea correcta
def seleccionar_opciones(list, title):
    while True: #se repite hasta que el usuario ingrese una opcion valida
        mostrar_opciones(list,title) # Se llana otra funcion para mostrar las opciones
        NumIngresado=(input("Por favor seleccione una opcion: "))
         #validacion para asegurar que el usuario ingrese un numero
        if not NumIngresado.isdigit():
            print("Por favor ingresa un número válido.")
            continue
        NumIngresado=int(NumIngresado)
        if 1 <= NumIngresado<= len(list):
            return list[NumIngresado - 1] #Retorna el elemnto seleccionado
        else:
            print("Número fuera de rango, intenta de nuevo.")    


if __name__ == "__main__":
    #Aqui hay varias cosas importates 
    print("Bienvenido a nuestro restaurante, por favor realice su orden")
    print("Por compras mayores a $50000, se aplica un descuento del 15%")
    #Estas variables reciben lo que la funcion seleccionar_opciones retorna, esta a su vez es la que 
    #pide todas las cosas al usuario , la funcion pide una lista y un titulo para mostrar,
    #lo que hace es acceder a la lista previamente creada que contiene los menus 
    entrada=seleccionar_opciones(entradas, "entradas")
    Platofuerte=seleccionar_opciones(PlatosFuertes, "platos fuertes")
    bebida=seleccionar_opciones(bebidas, "bebidas")
    postre=seleccionar_opciones(postres, "postres")
    #Teniendo el pedido en si , se llama la clase order con sus argumentos siendo los cuatro objetos
    #esto a traves de la variable que sirve como puente 
    Corden=order(entrada,Platofuerte,bebida,postre)
    #despues de que se llama order y a Corden se le asigna el objeto, se llama la funcion que imprime la orden
    Corden.show_order()
    #Funcion final que muestra lo pedido y el total a pagar
    print("Gracias por su compra, vuelva pronto")

    

    

