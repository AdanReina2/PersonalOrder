%include('header.tpl',login=login)
<h1>Distancia entre 2 puntos</h1>
<p>Entre {{posicion}} y {{nuevaposicion}} hay un total de {{r11.text[0]["elements"][0]["distance"]["text"]}}</p>
%include('foot.tpl')