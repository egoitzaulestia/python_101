class Empleado:
    def __init__(self, nombre, apellido, exp, pais, ciudad):
        self.nombre     = nombre
        self.apellido   = apellido
        self.exp        = exp
        self.pais       = pais
        self.ciudad     = ciudad
        self._salario  = 2000
        if self.exp >= 2:
            self._salario += 200
        elif self.exp >= 5:
            self._salario += 500
        elif self.exp >= 10:
            self._salario += 1000
        # self.__sueldo = self._salario # A revisar

    def calcular_salario(self):
        return self._salario

    def get_salario(self):
        return self._salario
