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

@get('/log')
def info_calendar():
  if token_valido():
    redirect("/perfil")
  else:
    response.set_cookie("token", '',max_age=0)
    oauth2 = OAuth2Session(client_id, redirect_uri=redirect_uri,scope=scope)
    authorization_url, state = oauth2.authorization_url('https://accounts.google.com/o/oauth2/auth')
    response.set_cookie("oauth_state", state)
    redirect(authorization_url)

@get('/callback')
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
        r2 = oauth2.get('https://www.googleapis.com/oauth2/v1/userinfo')
        doc = json.loads(r2.content)
        return '<p>%s</p><img src="%s"/><br/><a href="/logout">Cerrar</a>' % (doc["name"],doc["picture"])
    else:
        redirect('/calendar')

@get('/logout')
def salir():
    response.set_cookie("token", '',max_age=0)
    redirect('/log')  

@route('/listareventos')
def listareventos():
    if token_valido():
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        r3 = oauth2.get('https://www.googleapis.com/calendar/v3/users/me/calendarList')
        doc = json.loads(r3.content)
    return template('listareventos.tpl',doc=doc)

@route('/formularionuevoevento')
def formularionuevoevento():
    return template('formularionuevoevento.tpl')

@route('/nuevoevento',method='post')
def nuevoevento():
    if token_valido():
        idnewevent = request.forms.get('idnewevent')
        startevent = request.forms.get('startevent')
        endevent = request.forms.get('endevent')
        infoevent = request.forms.get('infoevent')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'
        payload = {'calendarID':idnewevent,'events':'events'}
        r4 = oauth2.post(url_base,params=payload,data={{
                                                        "end": {
                                                         "date": endevent
                                                        },
                                                        "start": {
                                                         "date": startevent
                                                        },
                                                        "summary": infoevent
                                                        }})
        estado = r4.status_code
        if estado == 200:
            return template('nuevoevento.tpl',estado='Evento Creado')
        else:
            return template('nuevoevento.tpl',estado='Evento no creado')

@route('/formularioborrarevento')
def formularioborrarevento():
    return template('formularioborrarevento.tpl')    
    
@route('/eliminarevento',method='post')
def eliminarevento():
    if token_valido():
        idoldcal = request.forms.get('idoldcal')
        idoldevent = request.forms.get('idoldevent')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'
        payload = {'calendarID':idoldcal,'events':'events','eventID':idoldevent}
        r6 = oauth2.delete(url_base,params=payload)
    
        estado = r6.status_code
        if estado == 204:
            return "<p>Evento eliminado</p>"
        else:
            return "<p>Evento no eliminado</p>"
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
