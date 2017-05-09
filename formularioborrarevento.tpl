%include('header.tpl',login=login)
<h1>Introduce los datos del evento que quieres eliminar</h1>
<form action="/listareventos2" method="post">
      <label><p>Calendario a usar: </p></label>
      <select name="idcal">
            % for i in lista:
                  <option value="{{contador}}">{{i}}</option>
                  contador = contador + 1
            % end
      </select>
      <br></br>
      <INPUT type="submit" value="Ver Eventos">
</form>
%include('foot.tpl')
