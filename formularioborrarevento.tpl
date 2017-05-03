%include('header.tpl')
<h1>Introduce los datos del evento que quieres eliminar</h1>
<form action="/eliminarevento" method="post">
      <label>ID del Calendario: </label>
      <INPUT type="text" name="idnewevent">
      <label>ID del evento: </label>
      <INPUT type="text" name="startevent">
      <INPUT type="submit" value="Eliminar Evento">
</form>
%include('foot.tpl')
