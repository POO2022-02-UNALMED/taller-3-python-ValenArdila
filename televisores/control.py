class Control:
    def __init__(self):
        self.__tv=None
    def turnOff(self):
        self.__tv.turnOff()
    def turnOn(self):
        self.__tv.turnOn()
    def canalUp(self):
        self.__tv.canalUp()
    def canalDown(self):
        self.__tv.canalDown()
    def volumenUp(self):
        self.__tv.volumenUp()
    def volumenDown(self):
        self.__tv.volumenDown()
    def setCanal(self,canal):
        self.__tv.setCanal(canal)
    def enlazar(self,televisor):
        self.__tv=televisor
        self.__tv.setControl(self)
    def getTv(self):
        return self.__tv