%include('header.tpl')
<h1>Crear nuevo evento</h1>
<form action="/nuevoevento" method="post">
      <label><p>Nombre del Calendario: </p></label>
      <INPUT type="text" name="idnewevent">
      <label><p>Inicio del evento: </p></label>
      <INPUT type="text" name="startevent">
      <label><p>Final del evento: </p></label>
      <INPUT type="text" name="endevent">
      <label><p>Nombre del evento: </p></label>
      <INPUT type="text" name="nameevent">
      <label><p>Localización del evento: </p></label>
      <INPUT type="text" name="locaevent">
      <br></br>
      <INPUT type="submit" value="Crear Evento">
</form>
%include('foot.tpl')
