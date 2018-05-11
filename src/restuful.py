from flask import Flask,jsonify,request
import requests
app=Flask(__name__)


languages=[{'name':"javascript"},
{'name':'python'},
{'name':'java'}
]


@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'its working '})


@app.route('/lang/',methods=['GET'])
def returnall():
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>',methods=['GET'])
def returnname(name):
    lang=[language for language in languages if language['name'] == name]
    #lang=[{'name':"javascript"}]

    return jsonify({'languages':lang[0]})

@app.route('/lang',methods=['POST'])
def addone():
    #abc=request.json['name']
    abc=request.get_json(force=True)
    #abc=None
    print(abc)
    if not abc:
        abc='c++'
    #language={'name':abc }
    #print(language)
    languages.append(abc)
    return jsonify({'languages':languages})



if __name__== '__main__':
    app.run(debug=True,port=8080)
