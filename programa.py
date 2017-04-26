from bottle import *
from lxml import etree
import requests

@route('/')
def consulta():
    return template("formulario.tpl")

@post('/resultado')
def resultado():
    city = request.forms.get('city')
    cate = request.forms.get('cate')
    url_base = "http://api.eventful.com/rest"
    k=open("key.txt","r")
    key = k.readline()
    k.close()
    payload = {'app_key':key, 'keywords':cate,'location':city,'date':'Future'}
    r = requests.get(url_base + '/events/search', params=payload)
    if r.status_code == 200:
        doc = etree.fromstring(r.text.encode('utf-8'))
        return template("resultado.tpl",doc=doc,city=city,cate=cate)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='0.0.0.0',port=8081)
