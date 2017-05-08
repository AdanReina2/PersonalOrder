%include('header.tpl')
<h1>Introduce el ID del calendario donde quieres crear el nuevo evento.</h1>
<form action="/nuevoevento" method="post">
      <label>Nombre del Calendario: </label>
      <INPUT type="text" name="idnewevent">
      <label>Inicio del evento: </label>
      <INPUT type="text" name="startevent">
      <label>Final del evento: </label>
      <INPUT type="text" name="endevent">
      <label>Nombre del evento: </label>
      <INPUT type="text" name="nameevent">
      <label>Localización del evento: </label>
      <INPUT type="text" name="locaevent">
      <br></br>
      <INPUT type="submit" value="Crear Evento">
</form>
%include('foot.tpl')
