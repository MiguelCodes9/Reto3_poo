## Este es un ejercicio que corresponde a la Clase 7: Herencia, cuando los objetos se parecen.

if __name__ == "__main__":
    ## Esa clase define el concepto de punto , dando una coordenada x y y  
    class Point:
      def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    ##Esta clase reune todos los metodos solicitados en el ejercicio
    class Rectangle:
      def __init__(self, width,height,point_center): #Atributos de la clase 
        self.width=width
        self.height=height
        self.point_center=point_center
      def compute_area(self):      #Aqui se multiplican los lados para obtener el area
        Area= self.width * self.height
        return Area
      def compute_perimeter(self): 
        perim = (self.width+self.height)*2
        return perim
      #Para determinar si un punto esta dentro o fuera del rectangulo
      def compute_interference_point(self, point): # Se comparan las coordenadas con los límites mínimo y máximo en X y Y
        x_min = self.point_center.x - self.width / 2
        x_max= self.point_center.x + self.width /2
        y_min= self.point_center.y - self.height/2
        y_max= self.point_center.y + self.height/2
        if x_min<= point.x <=x_max and y_min <= point.y <= y_max:
          return True 
        else:
          return False 
    class Square(Rectangle): #hereda de rectangle , usando dos lados y un punto 
      def __init__(self, side, center):
          super().__init__(center, side, side)  
#Ingreso de datos por parte del usuario
x_center=float(input("Por favor ingrese la coordenada x del centro del rectangulo ="))
y_center=float(input("Por favor ingrese la coordenada y del centro del rectangulo ="))
width_r=float(input("Por favor ingrese el ancho del rectangulo="))
height_r=float(input("Por favor ingrese la altura del rectangulo="))
center_r=Point(x_center,y_center)
#Se le asigna a la variable rect un objeto de la clase Rectangle
rect=Rectangle(width_r,height_r,center_r) 
#Cálculo del área y perímetro del rectángulo
area_rectangulo=rect.compute_area()
perimetro_rectangulo=rect.compute_perimeter()
#se imprimen los resultados
print("El area del rectangulo corresponde a",area_rectangulo, "unidades cuadradas")
print("El perimetro del rectangulo corresponde a ",perimetro_rectangulo)
#se le pide al usuario ingresar las coordenadas de un punto
p_x=float(input("Por favor ingrese la coordenada x de un punto= "))
p_y=float(input("Por favor ingrese la coordenada y de un punto= "))
#Se crea una variable point_v que es un objeto de la clase Point
point_v=Point(p_x,p_y)
p_imprimible=(p_x,p_y)
#verifica si compute_interference_point es True o False
if rect.compute_interference_point(point_v):
  print("El punto", p_imprimible, "esta dentro del rectangulo")
else:
  print("El punto", p_imprimible, "esta fuera del rectangulo")
