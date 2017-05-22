%include('header.tpl',login=login)
<h1 class="titulo">Listar Calendarios</h1>
<table>
%for a,b in zip(lista,lista2):
	<tr>
		<td>{{a}}</td>
      	<td><a href="/eliminarcalendario/{{b}}">Eliminar</a></td>
    </tr>
%end
</table>
<nav id="menu2" class="clearfix" role="navigation">
   	<ul> 
       	<li>
       		<a href="/formularionuevocalendario">Crear nuevo Calendario</a>
	 	</li>
    </ul>
</nav>
%include('foot.tpl')