# RESPUESTA AMAZON username y contraseñas
# funcion para validar el nombre, según la norma >= 6 caracteres
def validarNombre(nombre):
  LENGTH_NOMBRE = 6
  if len(nombre) < LENGTH_NOMBRE:
    return False
  else:
    return True

# funcion para validar la contraseña, según la norma >= 7 caracteres, not in lista de contrasseñas faciles
def validarPassword(password):
  LENGTH_PASSWORD = 7

  if password in ("password", "contraseña", "1234567", "qwerty"):
    print("La contraseña es demasiado fácil")
    return False
  elif len(password) < LENGTH_PASSWORD:
    print("La contraseña es muy corta ")
    return False
  else:
    return True


if __name__ == "__main__":

  valido = False
  while valido == False:
    nombre = input(
      "Introduce tu nombre, el nombre debe tener 6 o más caracteres ")
    valido = validarNombre(nombre)

  valido = False
  while valido == False:
    contrasena = input("Introduce tu contrasena ")
    valido = validarPassword(contrasena)

  print("Nombre y contraseña validos. Puedes entrar al programa ahora")
  print(f"Bienvenido {nombre} y contraseña {contrasena}")
