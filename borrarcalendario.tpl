%include('header.tpl',login=login)
%if r4.status_code == 204:
	<h1>Se ha eliminado correctamente el calendario</h1>
%else:
	<h1>No se ha eliminado correctamente el calendario</h1>
%end
%include('foot.tpl')
