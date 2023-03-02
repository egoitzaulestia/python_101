from common.get import *

# Programa main()
if __name__ == "__main__":
    usuario = get_usuario()
    edad = get_edad()
    password = get_password()

    print(f"Bienvenidos {usuario}. Tu edad es {edad} y tu contraseña es {password}")
    
