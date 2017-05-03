%include('header.tpl')
<h1>Introduce el ID del calendario donde quieres crear el nuevo evento.</h1>
<form action="/nuevoevento" method="post">
      <label>ID del Calendario: </label>
      <INPUT type="text" name="idnewevent">
      <label>Inicio del evento: </label>
      <INPUT type="text" name="startevent">
      <label>Final del evento: </label>
      <INPUT type="text" name="endevent">
      <label>Información del evento: </label>
      <INPUT type="text" name="infoevent">
</form>
%include('foot.tpl')
