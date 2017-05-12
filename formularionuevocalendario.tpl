%include('header.tpl',login=login)
<h1>Crear nuevo calendario</h1>
<form action="/nuevocalendario" method="post">
      <label><p>Nombre del nuevo caledario: </p></label>
      <INPUT type="text" name="nombrecalendario">
      <br></br>
      <INPUT type="submit" value="Crear Calendario">
</form>
%include('foot.tpl')