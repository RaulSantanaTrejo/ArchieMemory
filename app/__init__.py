import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS']) #loads the correct config

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/remember',methods=['POST'])
def remember():
    try:
        if not request.json:
            error_msg = "could not process json, received:  " + str(request.data)
            print(error_msg)
            return error_msg, 400
        memory = request.json

        db.session.add(Memory(memory['content'], memory['category']))
        db.session.commit()
        return "Added memory: {content} to database with category {category}".format(content=memory['content'], category= memory['category'])

    except Exception as e:
        error_msg = 'Error in remember endpoint: ' + str(e)
        print(error_msg)
        return error_msg

@app.route('/get_memory',methods=['GET'])
def get_memory():
    try:
        memory_id = request.args.get('id')
        memory_content = request.args.get('content')
        message = "Found memory with id: '{id}', content: '{content}' and category: '{category}'"

        if memory_id:
            memory = Memory.query.filter_by(id=memory_id).first()
            if memory is not None:
                return message.format(id=memory.id, content=memory.memory_content, category=memory.memory_category)

        if memory_content:
            memory = Memory.query.filter_by(memory_content=memory_content).first()
            if memory is not None:
                return message.format(id=memory.id, content=memory.memory_content, category=memory.memory_category)

        return "Couldn't find memory matching those parameters"


    except Exception as e:
        error_msg = 'Error while retrieving memory: ' + str(e)
        print(error_msg)
        return error_msg

@app.route('/forget',methods=['GET'])
def forget():
    try:
        memory_id = request.args.get('id')
        memory_content = request.args.get('content')
        message = "Deleted memory with id: '{id}', content: '{content}' and category: '{category}'"

        if memory_id:
            memory = Memory.query.filter_by(id=memory_id).first()
            db.session.delete(memory)
            db.session.commit()
            return message.format(id=memory.id, content=memory.memory_content, category=memory.memory_category)

        if memory_content:
            memory = Memory.query.filter_by(memory_content=memory_content).first()
            db.session.delete(memory)
            db.session.commit()
            return message.format(id=memory.id, content=memory.memory_content, category=memory.memory_category)

        return "Couldn't find memory matching those parameters"


    except Exception as e:
        error_msg = 'Error while retrieving memory: ' + str(e)
        print(error_msg)
        return error_msg

if __name__ == '__main__':
    app.run()
