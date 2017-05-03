%include('header.tpl')
<form action="/resultado" method="post">
      <label>Ciudad: </label>
      <INPUT type="text" name="city">
      <label>Categoria: </label>
      <INPUT type="text" name="cate">
      <INPUT>ID: </label>
      <INPUT type="text" name="id" placeholder={{client_id}}>
      <INPUT type="submit" value="Enviar">
</form>
%include('foot.tpl')
