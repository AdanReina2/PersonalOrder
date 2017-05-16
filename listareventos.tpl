%include('header.tpl',login=login)
<h1 class="titulo">Listar eventos</h1>
<table>
%for a,b,c in zip(lista,lista2,lista3):
	<tr>
		%if b == "null":
			<td>{{a}}</td>
			<td></td>
		%else:
			<td>{{a}}</td>
			<td><p>{{b}}</p><p><a href="/formulariomapa/{{b}}">Ver Distancia a este punto</p></td>
		%end
      	<td><a href="/formulariomodificareventos2/{{c}}/{{idcal}}">Modificar</a></td>
      	<td><a href="/eliminarevento/{{c}}/{{idcal}}">Eliminar</a></td>
    </tr>
%end
</table>
<nav id="menu2" class="clearfix" role="navigation">
   	<ul> 
       	<li>
       		<a href="/formularionuevoevento">Crear nuevo evento</a>
	 	</li>
    </ul>
</nav>
%include('foot.tpl')
