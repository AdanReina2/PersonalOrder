%include('header.tpl',login=login)
<h1>Distancia entre un lugar de busqueda y la localización del evento</h1>
%for a,b in zip(lista,lista2):
	{{idcal}}
    <a href="/formulariomodificareventos2/{{b}}/{{idcal}}">Ver mapa</a></td>
%end
%include('foot.tpl')