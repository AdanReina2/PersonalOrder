%include('header.tpl')
<h1>Listar eventos</h1>
%for a in {{nombres}}:
	{{a}}
%end
%include('foot.tpl')
