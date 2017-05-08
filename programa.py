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
    return template('inicio.tpl',key=key)

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

@route('/formulariolistareventos')
def formulariolistareventos():
    return template('formulariolistareventos.tpl')

@route('/listareventos',method='post')
def listareventos():
    if token_valido():
        idcal = request.forms.get('idcal')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars'+idcal+'/events'
        r3 = oauth2.get(url_base)
        doc = json.loads(r3.content)
        return doc

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
        r4 = oauth2.post(url_base,data=event,params=payload,headers=headers)
        return template('nuevoevento.tpl',estado=r4)
        
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
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idoldcal+'/events/'+idoldevent
        payload = {'key':key}
        r6 = oauth2.delete(url_base,params=payload)
    
        estado = r6.status_code
        if estado == 204:
            return template('eliminareventobien.tpl')
        else:
            return template('eliminareventomal.tpl')
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
