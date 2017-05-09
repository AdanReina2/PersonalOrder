%include('header.tpl',login=login)
<h1>Listar eventos</h1>
%for a in lista:
	<p>{{a}}</p>
%end
%include('foot.tpl')
