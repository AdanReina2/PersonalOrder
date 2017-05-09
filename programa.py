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
key = os.environ["KEY_API"]

@route('/')
def inicio():
    return template('inicio.tpl',key=key,login=token_valido())

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
        return template('datospersonales.tpl',doc=doc,login=token_valido())
    else:
        redirect('/calendar')

@get('/logout')
def salir():
    response.set_cookie("token", '',max_age=0)
    redirect('/log')  

def listarcalendarios():
    if token_valido():
        lista = []
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
        payload = {'key':key}
        r11 = oauth2.get(url_base,params=payload)
        doc = json.loads(r11.content)
        for i in doc["items"]:
            lista.append(i["summary"])
        return template('formularionuevoevento.tpl',lista=lista,login=token_valido())
    
@route('/formulariolistareventos')
def formulariolistareventos():
    return template('formulariolistareventos.tpl',login=token_valido())

@route('/listareventos',method='post')
def listareventos():
    if token_valido():
        lista = []
        idcal = request.forms.get('idcal')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idcal+'/events'
        payload = {'key':key}
        r3 = oauth2.get(url_base,params=payload)
        doc = json.loads(r3.content)
        for i in doc["items"]:
            lista.append(i["summary"])
        return template('listareventos.tpl',lista=lista,login=token_valido())

@route('/formularionuevoevento')
def formularionuevoevento():
    if token_valido():
        lista = []
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
        payload = {'key':key}
        r11 = oauth2.get(url_base,params=payload)
        doc = json.loads(r11.content)
        contador = 1
        for i in doc["items"]:
            lista.append(i["summary"])
        return template('formularionuevoevento.tpl',lista=lista,login=token_valido())

@route('/nuevoevento',method='post')
def nuevoevento():
    if token_valido():
        idnewevent = request.forms.get('idnewevent')
        startevent = request.forms.get('startevent')
        endevent = request.forms.get('endevent')
        infoevent = request.forms.get('infoevent')
        nameevent = request.forms.get('nameevent')
        locaevent = request.forms.get('locaevent')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        headers = {'Content-Type': 'application/json'}

        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idnewevent+'/events'
        event = {
            'summary': nameevent,
            'location': locaevent,
            'description': infoevent,
            'start': {
                'date': startevent,
            },
            'end': {
                'date': endevent,
            },
        }
        payload = {'key':key}
        r4 = oauth2.post(url_base,data=json.dumps(event),params=payload,headers=headers)
        return template('nuevoevento.tpl',estado=r4,login=token_valido())
        
@route('/formularioborrarevento')
def formularioborrarevento():
    return template('formularioborrarevento.tpl',login=token_valido())    
    
@route('/eliminarevento',method='post')
def eliminarevento():
    if token_valido():
        idoldcal = request.forms.get('idoldcal')
        idoldevent = request.forms.get('idoldevent')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idoldcal+'/events/'+idoldevent
        payload = {'key':key}
        r6 = oauth2.delete(url_base,params=payload)
    
        estado = r6.status_code
        if estado == 204:
            return template('eliminareventobien.tpl',login=token_valido())
        else:
            return template('eliminareventomal.tpl',login=token_valido())
    return template('eliminarevento.tpl',login=token_valido())

@route('/modificarevento')
def modificarevento():
    return template('modificarevento.tpl',login=token_valido())

@route('/nuevocalendario')
def nuevocalendario():
    return template('nuevocalendario.tpl',login=token_valido())

@route('/borrarcalendario')
def borrarcalendario():
    return template('borrarcalendario.tpl',login=token_valido())

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='0.0.0.0',port=argv[1])
