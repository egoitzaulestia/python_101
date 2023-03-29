acciones = {"SAN":3.14, "REP":14.1, "IBM":139, "MSFT":[1, 5, 6]}
print(type(acciones))
print(acciones)
acciones["REP"]
acciones["REP"] = 15
acciones["REP"]
acciones.update({"REP":21})
print(acciones["REP"])
acciones.update({"TEL":34})
acciones["TEL"]
print(acciones)

print("REP" in acciones)
if "REP" in acciones:
  print("Sí")

for key, value in acciones.items():
  print(key, value)

for key in acciones.keys():
  print(key)

for value in acciones.values():
  print(value)





  accionesEj = {"AENA.MC":143.75, "BBVA.MC":6.34, "REP.MC":14.22, "SAN.MC":3.324}
print(type(accionesEj))
print(accionesEj["BBVA.MC"])
accionesEj.update({"OHLA.MC":0.518, "ANE.MC":34.32, "TEF.MC":3.811})
print(accionesEj)

# sumaTotal = []
# for value in accionesEj.values():
#   if value == "SAN.MC":
#     accionesEj.pop()
#   sumaTotal.append(value)
# # sumaTotal.pop("SAN.MC")
# print(accionesEj)
# sum(sumaTotal)

total = 0
for key, value in accionesEj.items():
  if key != "SAN.MC":
    total += value

print(f"El total es ${total}")



import json
acciones = {"SAN":3.14, "REP":14.1, "IBM":139}


# para convertir un JSON en string
s = json.dumps(acciones)
print(type(s))
print(s)

# para convertir un string en Dicc
dicc = json.loads(s)
print(type(dicc))
print(dicc)


# import json
test = """{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}"""

s = json.loads(test)
print(type(s))
print(s)

dicc = json.dumps(test)
print(type(dicc))
print(dicc)






import pandas as pd

datos = {"SAN":3.14, "REP":14.1, "IBM":129}
series = pd.Series(datos)
print(series)
series.loc["REP"]
datos = [45, 23, 7, 5, 8, 9, 10]
series = pd.Series(datos)
print(series)
series.loc[4]
series.iloc[4]


datos = [45, 23, 7, 5, 8, 9, 10]
series = pd.Series(datos)
print(series.sum())
print(series.nsmallest(n=3))
series.mean()
series.describe()

series.head(2)
series.tail(2)
