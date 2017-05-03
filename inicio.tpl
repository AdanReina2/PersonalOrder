%include('header.tpl')
<h1>Bienvenido a Personal Order, ¿Que desea hacer?</h1>
<form action="/listareventos" method="get">
      <INPUT type="submit" value="Listar todos los eventos">
</form>
<form action="/formularionuevoevento" method="get">
      <INPUT type="submit" value="Crear un nuevo evento">
</form>
<form action="/eliminarevento" method="get">
      <INPUT type="submit" value="Eliminar un evento">
</form>
<form action="/modificarevento" method="get">
      <INPUT type="submit" value="Modificar un evento existente">
</form>
<form action="/nuevocalendario" method="get">
      <INPUT type="submit" value="Crear un nuevo calendario">
</form>
<form action="/borrarcalendario" method="get">
      <INPUT type="submit" value="Borrar un calendario">
</form>
<form action="/log" method="get">
      <INPUT type="submit" value="Ver información personal del usuario">
</form>
%include('foot.tpl')
