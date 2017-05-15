%include('header.tpl',login=login)
<h1>Se ha eliminado correctamente el calendario</h1>
{{estado.status_code}}
{{estado.text}}
%include('foot.tpl')
