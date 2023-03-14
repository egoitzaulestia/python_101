<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #0430aa;
  color: white;
}
    </style>
</head>
<body>
    <h1>Lista de Personas</h1>
    <!-- {% for persona in personas%}
        <table>
            <tr>
                <td>A</td>
                <td>{{persona}}</td>
            </tr>
        </table>
    {% endfor %} -->
    <table id = "customers">
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Edad</th>
        </tr>
        {% for empleado in empleados %}
            <tr>
                <td>{{empleado.id}}</td>
                <td>{{empleado.nombre}}</td>
                <td>{{empleado.apellido}}</td>
                <td>{{empleado.edad}}</td>
            </tr>
        {% endfor %}
    </table>
</body>
</html>
