%include('header.tpl')
<h1>Introduce el ID del calendario donde quieres crear el nuevo evento.</h1>
<form action="/nuevoevento" method="post">
      <select name="idnewevent">
            <option value="1">Windows Vista</option> 
            <option value="2">Windows 7</option> 
            <option value="3">Windows XP</option>
            <option value="10">Fedora</option> 
            <option value="11">Debian</option> 
            <option value="12">Suse</option> 
      </select>
      <!--<label>Nombre del Calendario: </label>
      <INPUT type="text" name="idnewevent">-->
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
