%include('header.tpl')
<h1>Introduce el ID del calendario donde quieres buscar los eventos</h1>
<form action="/listareventos" method="post">
      <label>Nombre del Calendario: </label>
      <INPUT type="text" name="idcal">
      <br></br>
      <INPUT type="submit" value="Crear Evento">
</form>
%include('foot.tpl')