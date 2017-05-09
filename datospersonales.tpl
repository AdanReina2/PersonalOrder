%include('header.tpl')
<h1>Bienvenido, estás en el sistema como {{doc["name"]}}</h1>
<img src="{{doc["picture"]}}"/>
<br></br>
<a id="site-description1" href="/logout">Cerrar Sesión</a>
<a id="site-description1" href="/">Menu Principal</a>
%include('foot.tpl')
