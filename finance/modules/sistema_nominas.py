# Calse Sistema_Nominas
class Sistema_Nominas:
    # Método calcular nóminas. Le pasamos un parámetro - una lista de de objetos de los distintos tipos de empleados/as
    def calcular_nominas(self, empleados):
        print("\n==================\nCalculando nominas\n==================\n")
        # Bucle for para recorrer la lista "empleados"
        for empleado in empleados:
            print(f"Nomina para : {empleado.nombre} {empleado.apellido} - {empleado.role}")
            print(f"- $ : {empleado.calcular_salario()}")
