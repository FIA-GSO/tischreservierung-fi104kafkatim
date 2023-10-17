import flask
from flask import request, json  # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify   # übersetzt python-dicts in json
import sqlite3
#from itertools import izip

app = flask.Flask(__name__)
app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
@app.errorhandler(404)
def page_not_found():
    return "<h1>404</h1><p>Es ist ein unbekannter Fehler aufgetreten.</p>", 404
@app.route('/api/restaurant/table_reservations/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('buchungssystem.sqlite')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_tables = cur.execute('SELECT anzahlPlaetze FROM tische;').fetchall()
    print(type(all_tables))
    all_reservations = cur.execute('SELECT * FROM reservierungen;').fetchall()
    reservationDict = dict.fromkeys(all_reservations)
    print(type(all_reservations))
    for reservation in reservationDict:
        print(reservation)
    return


def home():
    return jsonify(books)


app.run()