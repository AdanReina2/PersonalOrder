from bottle import *
from lxml import etree
import requests
from sys import argv
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from urlparse import parse_qs
import json

client_id = os.environ["client_id"]
client_secret = os.environ["client_secret"]
redirect_uri = 'https://personalorder.herokuapp.com/callback'
scope = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/userinfo.profile']
token_url = "https://accounts.google.com/o/oauth2/token"

@route('/')
def inicio():
    return template('inicio.tpl')

def token_valido():
  token = request.get_cookie("token", secret='some-secret-key')
  if token:
    token_ok = True
    try:
      oauth2 = OAuth2Session(client_id, token=token)
      r = oauth2.get('https://www.googleapis.com/oauth2/v1/userinfo')
    except TokenExpiredError as e:
      token_ok = False
  else:
    token_ok = False
  return token_ok

@get('/calendar')
def info_calendar():
  if token_valido():
    redirect("/perfil")
  else:
    response.set_cookie("token", '',max_age=0)
    oauth2 = OAuth2Session(client_id, redirect_uri=redirect_uri,scope=scope)
    authorization_url, state = oauth2.authorization_url('https://accounts.google.com/o/oauth2/auth')
    response.set_cookie("oauth_state", state)
    redirect(authorization_url)

@get('/oauth2callback')
def get_token():

  oauth2 = OAuth2Session(client_id, state=request.cookies.oauth_state,redirect_uri=redirect_uri)
  token = oauth2.fetch_token(token_url, client_secret=client_secret,authorization_response=request.url)
  response.set_cookie("token", token,secret='some-secret-key')
  redirect("/perfil")
  
@get('/perfil')
def info():
  if token_valido():
    token = request.get_cookie("token", secret='some-secret-key')
    oauth2 = OAuth2Session(client_id, token=token)
    r = oauth2.get('https://www.googleapis.com/oauth2/v1/userinfo')
    doc = json.loads(r.content)
    return '<p>%s</p><img src="%s"/><br/><a href="/logout">Cerrar</a>' % (doc["name"],doc["picture"])
  else:
    redirect('/calendar')

@get('/logout')
def salir():
  response.set_cookie("token", '',max_age=0)
  redirect('/calendar')  

@route('/listareventos')
def listareventos():
    return template('listareventos.tpl')

@route('/nuevoevento')
def nuevoevento():
    return template('nuevoevento.tpl')

@route('/eliminarevento')
def eliminarevento():
    return template('eliminarevento.tpl')

@route('/modificarevento')
def modificarevento():
    return template('modificarevento.tpl')

@route('/nuevocalendario')
def nuevocalendario():
    return template('nuevocalendario.tpl')

@route('/borrarcalendario')
def borrarcalendario():
    return template('borrarcalendario.tpl')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='0.0.0.0',port=argv[1])
