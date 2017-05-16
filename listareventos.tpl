%include('header.tpl',login=login)
<h1>Listar eventos</h1>
%for a,b in zip(lista,lista2):
	%if b == "null":
		<p>{{a}}</p>
	%else:
		<p>{{a}} en {{b}}<p>
	%end
%end
%include('foot.tpl')
