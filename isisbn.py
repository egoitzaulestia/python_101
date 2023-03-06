from is_isbn.is_isbn import is_isbn

# isbn = is_isbn.is_isbn(9780262537520)
# print(isbn)

with open("a1.txt", "r") as f:
    lista = f.readlines()

for i in lista:
    x = is_isbn(i)
    print(f"El isbn: {i} es {x}")
