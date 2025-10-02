# Reto3_poo
En este repo se encuentra el desarrollo del reto 3, a continuacion esta el diagrama de clases que se encuentran en el codigo acerca del menu de un restaurante.
Estas son las clases que se encuentran en el codigo:

```mermaid
classDiagram
direction TB


    class MenuItem {
        +float price 
        +string name

        +total_price()
        +__str__()
    }

    class StartDish {
        +float price
        +string name
        +string type
        
        +__str__()
	   
      
    }
    class MainDish{
        +float price
        +string name
        
        +__str__()





    }
    class Beverage{
	    +float price
        +float size 
        +string name
        
        +__str__()


	   
    }

    class Dessert {
       +float price
       +string name
       +string flavor
        

        +__str__()

        
        

    }

    class Order {
        +startdish boolean
        +maindish  boolean
        +beverage  boolean
        +dessert   boolean

        +total_order()
        +show_order()
}

````

