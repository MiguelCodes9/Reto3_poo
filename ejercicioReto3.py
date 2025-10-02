#Se define la clase Point y Line, con sus respectivos atributos y metodos
class Point:
        def __init__(self,x=0,y=0):
            self.x=x
            self.y=y    
class Line:
        def __init__(self,length,slope,start,end): #la clase line tiene varios atributos=
            self.length=length #largo de la linea
            self.slope=slope #pendiente de la linea
            self.start=start   #punto inicial
            self.end=end    #punto final
        def compute_length(self): #Para sacar su longitud es como si hiciera pitagoras o sacar la norma de un vector
            length= ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5
            return length
        def compute_slope(self):
            if (self.end.x-self.start.x)!=0: # para evitar la division entre cero
                slope=(self.end.y-self.start.y)/(self.end.x-self.start.x) #esta es la formula de la pendiente
                return slope
            else:
                return None 
        def compute_horizontal_cross(self):
            if (self.start.y * self.end.y)<0: # si los signos son diferentes, entonces cruza el eje horizontal
                return True
            elif self.start.y==0 or self.end.y==0: # si alguno de los puntos es cero, entonces tambien cruza el eje horizontal
                return True
            else:
                return False 
        def compute_vertical_cross(self):
            if (self.start.x * self.end.x)<0: # si los signos son diferentes, entonces cruza el eje vertical
                return True
            elif self.start.x==0 or self.end.x==0: # si alguno de los puntos es cero, entonces tambien cruza el eje vertical
                return True
            else:
                return False 
            
class Rectangule:
        #Uso dos lados para deniri el rectangulo, ya que es mas facil, ya que solo necesito dos lineas 
        def __init__(self,lado1, lado2):
            self.lado1=lado1          
            self.lado2=lado2
        #El perimetro es la suma de los lados por dos
        def compute_perimeter(self):
            perimetro=self.lado1.compute_length()*2 + self.lado2.compute_length()*2
            return perimetro
if __name__ == "__main__":
    # aqui dejo al usuario escojer si prefiere crear un rectangulo o solo una linea
    print("Por favor ingrese todos los datos acerca de las coordenadas de las puntas de las lineas=")
    desition=float(input("Si desea crear un rectangulo ingresando dos lineas,presione 1, si no presione 2:"))
    if desition <1 or desition >2:
        print("Opcion no valida, por favor intente de nuevo")
    elif desition==1:
     #Se crea un for en rango 2 ya que se necesitan dos lineas para crear el rectangulo
     #creo una lista para guardar las dos lineas
     lista_de_lineas=[]
     for i in range(2):
            #Ingreso de las coordenadas de los puntos iniciales 
            x1=float(input("Coordenada x inicial:"))
            y1=float(input("Coordenada y inicial:"))
            x2=float(input("Coordenada x final:"))
            y2=float(input("Coordenada y final:"))
            start_p=Point(x1,y1)
            end_p=Point(x2,y2)
            #se pone none ya que no se conocen esos atributos para este caso 
            linea=Line(None,None,start_p,end_p)
            lista_de_lineas.append(linea) # se agrega la linea a la lista
            #se llaman las funciones para mostrar las propiedades de cada linea
            print("Longitud de la linea", i+1,"es:", linea.compute_length())
            print("Pendiente de la linea", i+1,"es:", linea.compute_slope())
            print("La linea", i+1,"cruza el eje horizontal?", linea.compute_horizontal_cross())
            print("La linea", i+1,"cruza el eje vertical?", linea.compute_vertical_cross())
    #esta variable almacena el objeto rectangulo, usando las dos lineas de la lista, ya que se encuentran en las posiciones 0 y 1
     rect=Rectangule(lista_de_lineas[0],lista_de_lineas[1])
     print("El largo del rectangulo es:", lista_de_lineas[0].compute_length()) # Se llama a la funcion compute_length para mostrar el largo
     print("El ancho del rectangulo es:", lista_de_lineas[1].compute_length())
     print("El perimetro del rectangulo es:", rect.compute_perimeter())


     # Aqui solamente se crea una linea y se muestran sus propiedades
    elif desition==2:
            x1=float(input("Coordenada x inicial:"))
            y1=float(input("Coordenada y inicial:"))
            x2=float(input("Coordenada x final:"))
            y2=float(input("Coordenada y final:"))
            start_p=Point(x1,y1)
            end_p=Point(x2,y2)
            linea=Line(None,None,start_p,end_p)
            print("Longitud de la linea:", linea.compute_length())
            print("Pendiente de la linea:", linea.compute_slope())
            print("La linea cruza el eje horizontal?", linea.compute_horizontal_cross())
            print("La linea cruza el eje vertical?", linea.compute_vertical_cross())
