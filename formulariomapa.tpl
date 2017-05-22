%include('header.tpl',login=login)
<h1>Distancia entre un lugar de busqueda y la localización del evento</h1>
<form action="/vermapa/{{posicion}}/{{nuevaposicion}}" method="post">
      <label><p>Localización del destino: </p></label>
      <INPUT type="text" name="nuevaposicion">
      <br></br>
      <INPUT type="submit" value="Mandar los datos">
</form>
%include('foot.tpl')