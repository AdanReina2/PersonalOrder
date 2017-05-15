%include('header.tpl',login=login)
<h1>Eliminar un caledario</h1>
<form action="/borrarcalendario" method="post">
      <label><p>Calendario a eliminar: </p></label>
      <select name="idcal">
            % for a,b in zip(lista,lista2):
                  <option value="{{b}}">{{a}}</option>
            % end
      </select>
      <br></br>
      <INPUT type="submit" value="Eliminar Calendario">
</form>
%include('foot.tpl')