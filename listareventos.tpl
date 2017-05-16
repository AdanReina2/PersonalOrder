%include('header.tpl',login=login)
<h1>Listar eventos</h1>
%for a,b in zip(lista,lista2):
	<p>{{a}},{{b}}</p>
%end
%include('foot.tpl')
