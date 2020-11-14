from flask import make_response,jsonify,request,redirect,url_for,render_template
from . import app,db
from .models import Mew,MewSchema

@app.route('/')
def hello_world():
    mews=Mew.query.order_by(Mew.id.desc()).all()
    context={'mews':mews}
    return render_template('index.html',**context)


@app.route('/mews',methods=['POST'])
def create_new():
    data=request.get_json()

    new_mew=Mew(name=data.get('name'),content=data.get('content'))

    new_mew.create()

    mew=MewSchema().dump(new_mew)

    return make_response(jsonify({"message":"Created","mew":mew}))


@app.route('/mews',methods=['GET'])
def get_mews():
    mews=Mew.query.all()

    mew_schema=MewSchema(many=True)

    mew_list=mew_schema.dump(mews)

    return make_response(jsonify({"mews":mew_list}))



@app.shell_context_processor
def make_shell_context():
    return {'db':db,'Mew':Mew}