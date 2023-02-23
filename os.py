import os

print(os.environ)
print(os.getlogin())

print(os.getcwd())

path = os.getcwd()
print(os.listdir(path))
print(type(path))

os.chdir("../")
path = os.getcwd()
print(path)
print(os.listdir(path))
print(type(path))
