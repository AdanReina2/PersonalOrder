%include('header.tpl')
<h1>Listar eventos</h1>
%for a in lista:
	<a>{{a}}</a>
%end
%include('foot.tpl')
