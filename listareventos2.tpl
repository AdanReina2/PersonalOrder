%include('header.tpl',login=login)
<h1>Listar eventos</h1>
%for a in lista:
	{{a}}<a href="/eliminarevento"><img src="static/images/cancel.png"></a>
%end
%include('foot.tpl')