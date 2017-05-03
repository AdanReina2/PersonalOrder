from bottle import get, post, route, run, template
from lxml import etree
import requests
from sys import argv
from oauth2client.contrib.appengine import AppAssertionCredentials

credentials = AppAssertionCredentials('https://www.googleapis.com/auth/sqlservice.admin')

@route('/')
def consulta():
    return template("formulario.tpl")

@route('/resultado')
def resultado():
    print "Hola"

run(host='0.0.0.0',port=argv[1])
