from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import json
from auth import auth

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = auth['DB_key']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)

logs = Base.classes.logs


@app.route('/api', methods=['GET'])
def api():
    print(request.headers)
    if request.headers['Auth'] == auth['API_key']:
        print(dict(request.form))
        columns = logs.__table__.columns.keys()
        if request.form['multipleNicks'] == 'True':
            lines = db.session.query(logs). \
                filter_by(window=request.form['window']). \
                filter(logs.nick.in_(json.loads(request.form['nick']))). \
                order_by(logs.id)
        else:
            lines = db.session.query(logs). \
                filter_by(window=request.form['window']). \
                filter_by(nick=request.form['nick']). \
                order_by(logs.id)
        if request.form['date-start']:
            lines = lines.filter(logs.created_at >= request.form['date-start'])
        if request.form['date-end']:
            lines = lines.filter(logs.created_at <= request.form['date-end'])
        response = {
            'query': request.form,
            'body':  [{column: line.__dict__[column] for column in columns} for line in lines],
        }
        response['length'] = len(response['body'])

        return response
    else:
        return 'HTTP 401 Unauthorized '


if __name__ == '__main__':
    app.run()

