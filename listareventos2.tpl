%include('header.tpl',login=login)
<h1>Listar eventos</h1>
%for a,b in zip(lista,lista2):
	<form action="/nuevoevento" method="post">
		<select name="idnewcal">
            <option value="{{idcal}}">{{idcal}}</option>
      	</select>
		<select name="idevent">
            % for i in lista:
                  <option value="{{b}}">{{a}}</option>
            % end
      	</select>
      	<INPUT type="submit" value="Eliminar Evento">
	</form>
	<p>{{a}},{{b}}</p>
%end
%include('foot.tpl')