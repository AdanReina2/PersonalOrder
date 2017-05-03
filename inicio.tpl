%include('header.tpl')
<h1>Bienvenido a Personal Order, ¿Que desea hacer?</h1>
<form action="/listareventos" method="post">
      <INPUT type="submit" value="Listar todos los eventos">
</form>
<form action="/nuevoevento" method="post">
      <INPUT type="submit" value="Crear un nuevo evento">
</form>
<form action="/eliminarevento" method="post">
      <INPUT type="submit" value="Eliminar un evento">
</form>
<form action="/modificarevento" method="post">
      <INPUT type="submit" value="Modificar un evento existente">
</form>
<form action="/nuevocalendario" method="post">
      <INPUT type="submit" value="Crear un nuevo calendario">
</form>
<form action="/borrarcalendario" method="post">
      <INPUT type="submit" value="Borrar un calendario">
</form>
%include('foot.tpl')
