%include('header.tpl')
<h1>Listar eventos</h1>
%for a in lista:
	<p>{{a}}</p>
	<br></br>
%end
%include('foot.tpl')
