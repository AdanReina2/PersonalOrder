%include('header.tpl',login=login)
<h1>Crear nuevo evento</h1>
<form action="/modificareventos" method="post">
      <label><p>Nueva fecha de inicio: </p></label>
      <INPUT type="text" name="startevent">
      <label><p>Nueva fecha de final: </p></label>
      <INPUT type="text" name="endevent">
      <label><p>Nueva nombre del evento: </p></label>
      <INPUT type="text" name="nameevent">
</form>
<a href="/modificarevento/{{idevent}}/{{idcal}}">Modificar Evento</a>
%include('foot.tpl')