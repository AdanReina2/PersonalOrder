%include('header.tpl',login=login)
<h1>Listar eventos</h1>
%for a,b in zip(lista,lista2):
	<form action="/nuevoevento" method="post">
		<select name="idcal">
            <option value="{{idcal}}">{{idcal}}</option>
      	</select>
		<select name="idevent">
            % for i in lista:
                  <option value="{{b}}">{{a}}</option>
            % end
      	</select>
      	<INPUT type="submit" value="Eliminar Evento">
	</form>
%end
%include('foot.tpl')