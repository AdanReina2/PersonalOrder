%include('header.tpl',login=login)
<h1>Crear un nuevo evento</h1>
% if estado.status_code == 200:
	<p>Se ha creado correctamente el evento {{nameevent}} en el calendario {{idnewevent}}</p>
% else:
	{{estado.status_code}}
	{{estado.text}}
	<p>No se ha creado correctamente el evento {{nameevent}} en el calendario {{idnewevent}}</p>
% end
%include('foot.tpl')
