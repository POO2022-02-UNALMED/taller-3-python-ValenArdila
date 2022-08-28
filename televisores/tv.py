from televisores.control import Control
from televisores.marca import Marca
class TV():
    __numTV=0
    def __init__(self,marca,estado):
        self.__marca=marca
        self.__canal=1
        self.__precio=500
        self.__estado=estado
        self.__volumen=1
        self.__control=None
        TV.__numTV+=1
    def setMarca(self,marca):
        if isinstance(marca,Marca):
            self.__marca=marca
    def getMarca(self):
        return self.__marca
    def setControl(self,control):
        if isinstance(control,Control):
            self.__control=control
    def getControl(self):
        return self.__control
    def setPrecio(self,precio):
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    def setVolumen(self,volumen):
        if(self.__estado==True and volumen>=0 and volumen <=7):
            self.__volumen=volumen
    def getVolumen(self):
        return self.__volumen
    def setCanal(self,canal):
        if(self.__estado==True and canal>=1 and canal<=120):
            self.__canal=canal
    def getCanal(self):
        return self.__canal
    def setNumTV(cls,numTV):
        cls.__numTV=numTV
    def getNumTV(cls):
        return cls.__numTV
    def turnOff(self):
        self.__estado=False
    def turnOn(self):
        self.__estado=True
    def getEstado(self):
        return self.__estado
    def canalUp(self):
        if(self.__estado==True and self.__canal<120):
            self.__canal+=1
    def canalDown(self):
        if(self.__estado==True and self.__canal>1):
            self.__canal-=1
    def volumenUp(self):
        if(self.__estado==True and self.__volumen<7):
            self.__volumen+=1
    def volumenDown(self):
        if(self.__estado==True and self.__volumen>0):
            self.__volumen-=1