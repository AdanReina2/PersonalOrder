%include('header.tpl',login=login)
<h1>Listar eventos</h1>
%for a,b in zip(lista,lista2):
	<form action="/eliminarevento" method="post">
		<select name="idnewcal">
            <option value="{{idcal}}">{{idcal}}</option>
      	</select>
		<select name="idevent">
            <option value="{{b}}">{{a}}</option>
      	</select>
      	<INPUT type="submit" value="Eliminar Evento">
	</form>
%end
%include('foot.tpl')