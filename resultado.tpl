%include('header.tpl')
<h1>Eventos de {{city}} de {{cate}}</h1>
<ul>
	% for t,d,l in zip(doc.xpath("//title"), doc.xpath("//start_time"), doc.xpath("//venue_name")):
	      <li>{{t.text}}
	      		<ul>
	      			<li>El día {{d.text[8:10]}} del {{d.text[5:7]}}.</li>
	      			<li>En {{l.text}}</li>
	      		</ul>
	      </li>
	% end
</ul>
%include('foot.tpl')