%include('header.tpl',login=login)
<h1>Bienvenido, estás en el sistema como {{doc["name"]}}</h1>
<img src="{{doc["picture"]}}"/>
<br></br>
<nav id="menu2" class="clearfix" role="navigation">
        <ul> 
            <li><a href="/logout">Cerrar Sesión</a></li>
            <li><a href="/">Menu Principal</a></li>
        </ul>
</nav>
%include('foot.tpl')
