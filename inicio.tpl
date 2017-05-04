%include('header.tpl')
<h1>Bienvenido a Personal Order, ¿Que desea hacer?{{key}}</h1>
<form action="/listareventos" method="get">
      <INPUT style="border: #000 2px solid;background-color: red" type="submit" value="Listar todos los eventos">
</form>
<form action="/formularionuevoevento" method="get">
      <INPUT style="border: #000 2px solid;background-color: red"" type="submit" value="Crear un nuevo evento">
</form>
<form action="/formularioborrarevento" method="get">
      <INPUT style="border: #000 2px solid;background-color: red" type="submit" value="Eliminar un evento">
</form>
<form action="/modificarevento" method="get">
      <INPUT style="border: #000 2px solid;background-color: red" type="submit" value="Modificar un evento existente">
</form>
<form action="/nuevocalendario" method="get">
      <INPUT style="border: #000 2px solid;background-color: red" type="submit" value="Crear un nuevo calendario">
</form>
<form action="/borrarcalendario" method="get">
      <INPUT style="border: #000 2px solid;background-color: red" type="submit" value="Borrar un calendario">
</form>
<form action="/log" method="get">
      <INPUT style="border: #000 2px solid;background-color: red" type="submit" value="Ver información personal del usuario">
</form>
%include('foot.tpl')
