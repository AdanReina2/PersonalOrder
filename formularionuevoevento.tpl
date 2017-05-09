%include('header.tpl',login=login)
<h1>Crear nuevo evento</h1>
<form action="/nuevoevento" method="post">
      <select name="idnewevent">
            % for i in lista:
                  <option value="{{contador}}">{{i["summary"]}}</option>
                  contador = contador + 1
            % end
      </select>
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
