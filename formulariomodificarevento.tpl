%include('header.tpl',login=login)
<h1>Seleccionar el calendario para modificar los eventos:</h1>
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