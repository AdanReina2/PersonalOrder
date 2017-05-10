%include('header.tpl',login=login)
<h1>Listar eventos</h1>
<table>
%for a,b in zip(lista,lista2):
	<tr>
		<td>{{idcal}}</td>
      	<td>{{a}}</td>
      	<td><a href="/eliminarevento/{{b}}/{{idnewcal}}">Eliminar</a></td>
    </tr>
%end
</table>
%include('foot.tpl')