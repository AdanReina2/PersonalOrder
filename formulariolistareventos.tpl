%include('header.tpl')
<h1>Listar eventos del calendario especificado</h1>
<form action="/listareventos" method="post">
      <label>Nombre del Calendario: </label>
      <INPUT type="text" name="idcal">
      <br></br>
      <INPUT type="submit" value="Listar Eventos">
</form>
