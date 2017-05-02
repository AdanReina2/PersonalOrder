from bottle import *
from lxml import etree
import requests
from sys import argv

@route('/')
def consulta():
    return template("formulario.tpl")

@route('/resultado',method="post")
def resultado():
    print "Hola"

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='0.0.0.0',port=argv[1])
