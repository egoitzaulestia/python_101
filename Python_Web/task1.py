from datetime import date, daytime

today = date.today()
# now = daytime.now()

d1 = today.strftime("%d/%m/%Y")
# t1 = now.strftime("%h/%m/%s")

sText = d1 + "," + "Mensaje al administrador"

sText = "Mensaje al administrador"

with open("results.txt", "a") as f:
    f.write(sText)
    f.write("\n")
