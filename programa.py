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
            if i["accessRole"] == "owner":
                lista.append(i["summary"])
        return template('formularionuevoevento.tpl',lista=lista,login=token_valido())
    
@route('/formulariolistareventos')
def formulariolistareventos():
    if token_valido():
        lista = []
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
        payload = {'key':key}
        r11 = oauth2.get(url_base,params=payload)
        doc = json.loads(r11.content)
        for i in doc["items"]:
            if i["accessRole"] == "owner":
                lista.append(i["summary"])
        return template('formulariolistareventos.tpl',lista=lista,login=token_valido())

@route('/listareventos',method='post')
def listareventos():
    if token_valido():
        lista = []
        lista2 = []
        lista3 = []
        idcal = request.forms.get('calendario')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idcal+'/events'
        payload = {'key':key}
        r3 = oauth2.get(url_base,params=payload)
        doc = json.loads(r3.content)
        for i in doc["items"]:
            lista.append(i["summary"])
            if "location" in i: 
                lista2.append(i["location"])
            else:
                lista2.append("null")
            lista3.append(i["id"])
        return template('listareventos.tpl',lista=lista,lista2=lista2,lista3=lista3,idcal=idcal,login=token_valido())

@route('/listareventos2',method='post')
def listareventos():
    if token_valido():
        lista = []
        lista2 = []
        idcal = request.forms.get('idcal')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idcal+'/events'
        payload = {'key':key}
        r13 = oauth2.get(url_base,params=payload)
        doc = json.loads(r13.content)
        for i in doc["items"]:
            lista.append(i["summary"])
            lista2.append(i["id"])
        return template('listareventos2.tpl',lista=lista,lista2=lista2,login=token_valido(),idcal=idcal)

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
        for i in doc["items"]:
            if i["accessRole"] == "owner":
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
        return template('nuevoevento.tpl',estado=r4,login=token_valido(),idnewevent=idnewevent,nameevent=nameevent)
        
@route('/formularioborrarevento')
def formularioborrarevento():
    if token_valido():
        lista = []
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
        payload = {'key':key}
        r12 = oauth2.get(url_base,params=payload)
        doc = json.loads(r12.content)
        for i in doc["items"]:
            if i["accessRole"] == "owner":
                lista.append(i["summary"])
        return template('formularioborrarevento.tpl',lista=lista,login=token_valido(),doc=doc)    
    
@route('/eliminarevento/<idevent>/<idcal>',method='get')
def eliminarevento(idevent,idcal):
    if token_valido():
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idcal+'/events/'+idevent
        payload = {'key':key}
        r6 = oauth2.delete(url_base,params=payload)
    
        estado = r6.status_code
        if estado == 204:
            return template('eliminareventobien.tpl',login=token_valido())
        else:
            return template('eliminareventomal.tpl',login=token_valido())
    return template('eliminarevento.tpl',login=token_valido())

@route('/formulariomodificarevento')
def formulariomodificarevento():
    if token_valido():
        lista = []
        lista2 = []
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
        payload = {'key':key}
        r11 = oauth2.get(url_base,params=payload)
        doc = json.loads(r11.content)
        for i in doc["items"]:
            if i["accessRole"] == "owner":
                lista.append(i["summary"])
                lista2.append(i["id"])
        return template('formulariomodificarevento.tpl',lista=lista,login=token_valido())

@route('/listareventos3',method='post')
def listareventos():
    if token_valido():
        lista = []
        lista2 = []
        idcal = request.forms.get('idcal')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idcal+'/events'
        payload = {'key':key}
        r13 = oauth2.get(url_base,params=payload)
        doc = json.loads(r13.content)
        for i in doc["items"]:
            lista.append(i["summary"])
            lista2.append(i["id"])
        return template('listareventos3.tpl',lista=lista,lista2=lista2,login=token_valido(),idcal=idcal)

@route('/formulariomodificareventos2/<idevent>/<idcal>',method='get')
def formulariomodificarevento(idevent,idcal):
    if token_valido():
        return template('formulariomodificareventos2.tpl',login=token_valido(),idevent=idevent,idcal=idcal)

@route('/modificarevento/<idevent>/<idcal>',method='post')
def modificarevento(idevent,idcal):
    if token_valido():
        startevent = request.forms.get('startevent')
        endevent = request.forms.get('endevent')
        nameevent = request.forms.get('nameevent')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        headers = {'Content-Type': 'application/json'}
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idcal+'/events/'+idevent
        event = {
            'summary': nameevent,
            'start': {
                'date': startevent,
            },
            'end': {
                'date': endevent,
            },
        }
        payload = {'key':key}
        datos = json.dumps(event)
        r4 = oauth2.put(url_base,data=datos,params=payload,headers=headers)
        return template('modificarevento.tpl',estado=r4,login=token_valido(),idevent=idevent,nameevent=nameevent,startevent=startevent,endevent=endevent,idcal=idcal,datos=datos)
    return template('modificarevento.tpl',login=token_valido())

@route('/formulariolistarcalendarios')
def formulariolistarcalendarios():
    if token_valido():
        lista = []
        lista2 = []
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
        payload = {'key':key}
        r11 = oauth2.get(url_base,params=payload)
        doc = json.loads(r11.content)
        for i in doc["items"]:
            if i["accessRole"] == "owner":
                lista.append(i["summary"])
                lista2.append(i["id"])
        return template('formulariolistarcalendarios.tpl',login=token_valido(),lista=lista,lista2=lista2)

@route('/formularionuevocalendario')
def formulariomodificarevento():
    if token_valido():
        return template('formularionuevocalendario.tpl',login=token_valido())

@route('/nuevocalendario',method='post')
def nuevocalendario():
    if token_valido():
        nombrecalendario = request.forms.get('nombrecalendario')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        headers = {'Content-Type': 'application/json'}
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'
        event = {
            'summary': nombrecalendario,
        }
        payload = {'key':key}
        r4 = oauth2.post(url_base,data=json.dumps(event),params=payload,headers=headers)
        return template('nuevocalendario.tpl',login=token_valido(),nombrecalendario=nombrecalendario)
    return template('nuevocalendario.tpl',login=token_valido())

@route('/formularioborrarcalendario')
def formulariomodificarevento():
    if token_valido():
        lista = []
        lista2 = []
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
        payload = {'key':key}
        r11 = oauth2.get(url_base,params=payload)
        doc = json.loads(r11.content)
        for i in doc["items"]:
            if i["accessRole"] == "owner":
                lista.append(i["summary"])
                lista2.append(i["id"])
        return template('formularioborrarcalendario.tpl',lista=lista,lista2=lista2,login=token_valido())

@route('/borrarcalendario/<idcal>', method='get')
def borrarcalendario(idcal):
    if token_valido():
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://www.googleapis.com/calendar/v3/calendars/'+idcal
        payload = {'key':key}
        r4 = oauth2.delete(url_base,params=payload)
        return template('borrarcalendario.tpl',login=token_valido(),estado=r4)

@route('/formulariomapa/<posicion>',method='get')
def formulariomapa(posicion):
    if token_valido():
        return template('formulariomapa.tpl',posicion=posicion,login=token_valido())

@route('/vermapa/<posicion>',method='post')
def formulariomapa(posicion):
    if token_valido():
        nuevaposicion = request.forms.get('nuevaposicion')
        token = request.get_cookie("token", secret='some-secret-key')
        oauth2 = OAuth2Session(client_id, token=token)
        url_base = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+posicion+'&destinations='+nuevaposicion
        payload = {'key':key}
        r11 = requests.get(url_base,params=payload)
        a = r11.text
        b = a.get("rows")
        c = b.get("elements")
        distacia = c.get("distance").get("text")
        duracion = c.get("duration").get("text")
        return template('vermapa.tpl',posicion=posicion,nuevaposicion=nuevaposicion,duracion=duracion,distancia=distancia,login=token_valido())

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='0.0.0.0',port=argv[1])
