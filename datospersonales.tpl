%include('header.tpl')
<h1>Bienvenido, estás en el sistema como {{doc["name"]}}</h1>
<img src="{{doc["picture"]}}"/>
<a href="/logout">Cerrar Sesión</a>
<a href="/">Menu Principal</a>
%include('foot.tpl')
