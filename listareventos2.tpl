%include('header.tpl',login=login)
<h1>Listar eventos</h1>
%for a,b in zip(lista,lista2):
	{{a}}<form action="/eliminarevento/{{b}}" method="post"><INPUT type="submit" value="Borrar Evento"></form>
	<br>
%end
%include('foot.tpl')