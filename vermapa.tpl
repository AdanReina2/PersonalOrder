%include('header.tpl',login=login)
<h1>Distancia entre {{posicion}} y {{nuevaposicion}}</h1>
<p>Distancia entre los dos puntos: {{distancia*1,60934}}</p>
<p>Tiempo de viaje: {{duracion}}</p>
%include('foot.tpl')