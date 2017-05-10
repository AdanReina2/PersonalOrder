%include('header.tpl',login=login)
<h1>Listar eventos del calendario especificado</h1>
<form action="/listareventos" method="post">
	<label>Nombre del Calendario: </label>
	<select name="calendario">
		%for a in lista:
           	<option value="{{a}}">{{a}}</option>
        %end
    </select>
    <br></br>
	<INPUT type="submit" value="Listar Eventos">
</form>
