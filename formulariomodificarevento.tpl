%include('header.tpl',login=login)
<h1>Crear nuevo evento</h1>
<form action="/listareventos3" method="post">
      <label><p>Calendario a usar: </p></label>
      <select name="idcal">
            % for i in lista:
                  <option value="{{i}}">{{i}}</option>
            % end
      </select>
      <br></br>
      <INPUT type="submit" value="Ver Eventos">
</form>
%include('foot.tpl')