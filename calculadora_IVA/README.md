# Prototipo aplicación "Calculadora IVA" para el Banco Santander
---
Prototipo para facilitar al usuario la posibilidad de sumar el precio del IVA a un precio sin IVA y restar el precio del IVA a un precio con IVA. 

---

## El prototipo deberá facilitar al usuario:
   ### 1 _ Calcular la suma del IVA a un precio que no lleva IVA.
     + Para ello facilitar al usuario: 
       - Introducir precio sin IVA
       - Introducir del porcentaje de IVA
   ### 2 _ Calcular la resta del iva a un precio que incluye iva.
     + Para ello facilitar al usuario: 
       - Introducir precio toral con IVA
       - Introducir porcentaje del IVA que lleva el producto
___

## Pruebas del prototipo realizadas
El orden de los datos de input: 
  + Sumar IVA (precio sin IVA + porcentaje de IVA del precio sin IVA), Restar IVA (precio con IVA - porcentaje de IVA del precio con IVA).

El orden de los datos del output esperado:
  + Suma (Precion con IVA), Resta (Precio sin IVA)

El orden de los datos del output actual:
  + Suma (Precion con IVA), Resta (Precio sin IVA) 

---
|  Tests   |  Input                          |  Expected Output   |  Actaul Output   |  PASS / FAIL |
|  ---     |  ---                            |  ---               |  ---             |  ---         |
|  Test 1  |  (100€  + 21%) , -              |  121€  , -         |  121€  , -       |  PASS        |
|  Test 2  |  (100€  + 21%) , (100€  - 21%)  |  121€  ,  17.36€   |  121€  ,  44.59€ |  FAIL        |
|  Test 3  |  (100€  + 21%) , (100€  - 21%)  |  121€  ,  17.36€   |  121€  ,  62.32€ |  FAIL        |
|  Test 4  |  (100€  + 21%) , (100€  - 21%)  |  121€  ,  82,64€   |  121€  ,  82,64€ |  PASS        |
|  Test 5  |  (250€  + 10%) , (250€  - 10%)  |  275€  , 227,27€   |  275€  , 227,27€ |  PASS        |
|  Test 6  |  (9.95€ +  4%) , (3.41€ -  4%)  |  10.35€,   3,28€   |  10.35€,   3,28€ |  PASS        |
