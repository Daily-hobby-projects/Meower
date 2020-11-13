from flask import make_response,jsonify,request,redirect,url_for,render_template
from . import app,db
from .models import Mew,MewSchema

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/mews',methods=['POST'])
def create_new():
    data=request.get_json()

    print(f"\n\n{data}")

    new_mew=Mew(name=data.get('name'),content=data.get('content'))

    new_mew.create()

    return make_response(jsonify({"message":"Created"}))


@app.route('/mews',methods=['GET'])
def get_mews():
    mews=Mew.query.all()

    mew_schema=MewSchema(many=True)

    mew_list=mew_schema.dump(mews)

    return make_response(jsonify({"mews":mew_list}))



@app.shell_context_processor
def make_shell_context():
    return {'db':db,'Mew':Mew}