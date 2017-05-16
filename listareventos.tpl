%include('header.tpl',login=login)
<h1>Listar eventos</h1>
<table>
%for a,b,c in zip(lista,lista2,lista3):
	<tr>
		%if b == "null":
			<td>{{a}}</td>
			<td></td>
		%else:
			<td>{{a}}</td>
			<td>{{b}}</td>
		%end
      	<td><a href="/formulariomodificareventos2/{{c}}/{{idcal}}">Modificar</a></td>
      	<td><a href="/eliminarevento/{{c}}/{{idcal}}">Eliminar</a></td>
    </tr>
%end
</table>
%include('foot.tpl')
