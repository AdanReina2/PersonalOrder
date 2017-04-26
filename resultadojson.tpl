%include('header.tpl')
<h1>Eventos de {{city}} de {{cate}}</h1>
<ul>
	% for d in doc["events"]["event"]:
	      <li>{{d["title"]}}
	      		<ul>
	      			<li>El día {{d["start_time"][8:10]}} del {{d["start_time"][5:7]}}.</li>
	      			<li>En {{d["venue_name"]}}</li>
	      		</ul>
	      </li>
	% end
</ul>
%include('foot.tpl')