class vehiculo():
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    def __str__(self):
        return "color es {},{} ruedas".format(self.color,self.ruedas)
class coche(vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
         return "{}la velocidad es {}, {} cilindrada".format(super().__str__(), self.velocidad, self.cilindrada)
class camioneta(vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
        self.carga=carga
        
    def __str__(self):
        return "la velocidad es {}, {} cilindrada,la carga es {}".format(super().__str__(),self.velocidad,self.cilindrada,self.carga)
class bicicleta(vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo=tipo
    def __str__(self):
        return "{} el tipo es {}".format(super().__str__(),self.tipo)
class motocicleta(vehiculo):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.tipo=tipo
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return "{} el tipo es {},la velocidad es {}, la cilindrada es {}".format(super().__str__(),self.tipo,self.velocidad,self.cilindrada)
vehiculos =[
    coche("rojo",4,180,1600),
    camioneta("azul",4,120,2000,1000),
    bicicleta("verde",2,"montaña"),
    motocicleta("negro",2,"deportiva",200,1000)
] 
def catalogar(vehiculos,ruedas =None):
    for vehiculo in vehiculos:
        if ruedas is None:
            print(f"{type(vehiculo).__name__}:{vehiculo}")
        else:
            print(f"{type(vehiculo).__name__}:{vehiculo}")
print("Mostrando todos los vehículos:")
catalogar(vehiculos)
print("\nFiltrando por 2 ruedas:")
catalogar(vehiculos, 2)
print("\nFiltrando por 4 ruedas:")
catalogar(vehiculos, 4)