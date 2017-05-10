%include('header.tpl',login=login)
<h1>Listar eventos del calendario especificado</h1>
<form action="/listareventos" method="post">
	<label>Nombre del Calendario: </label>
	%for a in lista:
		<select name="calendario">
            <option value="{{a}}">{{a}}</option>
      	</select>
	%end
	<INPUT type="submit" value="Eliminar Evento">
</form>
