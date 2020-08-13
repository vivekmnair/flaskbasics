from newproject import app
from flask import Flask, render_template, request, redirect, url_for, flash
from newproject.forms import PostForm

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/getusers',methods=['POST', 'GET'])
def getusers():
    
    users=[]
    dbusers=User.query.all()
    try:
        for user in dbusers:
            dict = {"name":user.username,"email":user.email,"id":user.id}
            users.append(dict)
    except Exception as e:
        print(e)
    return jsonify(users)

@app.route('/usersaveform',methods=['POST', 'GET'])
def usersaveform():
    msg = ""
    status = 1
    try:
        data = request.get_json()
        print(data)
        user = User.query.filter_by(username= data["name"]).first()
        if(user):
            str1={"status":"fail"}
            msg = "username already exists"
        else:
            user = User.query.filter_by(email= data["email"]).first()
            if(user):
                status= 0
                msg = "email already exists"
            else:
                user = User(username=data["name"], email=data['email'], password=data['password'])
                db.session.add(user)
                db.session.commit()
                print("flask insde save users")
                msg="successfully done"

    
    except Exception as e:
            print(e)
            status= 0
            msg = "error found"
    str1={"status":status, "message": msg}
    print(msg)
    return str1

@app.route('/deleteuserform',methods=['DELETE', 'GET'])
def deleteuserform():
    users=[]
    try:
        print("inside")
        userid = request.args.get('userid')
        print(userid)
        user=User.query.get_or_404(userid)
        db.session.delete(user)
        db.session.commit()
        str1={"status":"success"}
        
        dbusers=User.query.all()
        for user in dbusers:
            dict = {"name":user.username,"email":user.email,"id":user.id}
            users.append(dict)
    except Exception as e:
        print(e)
        str1={"status":"fail"}
    return jsonify(users)
    
@app.route('/edituserform',methods=['POST', 'GET'])
def edituserform():
    users=[]
    message=""
    try:
        id = request.args.get('userid')
        user = User.query.get_or_404(id)
        if(user):
            dict = {"id":user.id,"name":user.username,"email":user.email,"password":user.password}
            users.append(dict)
            message="success"
    except Exception as e:
        print(e)
        message="error"
    retdata={"msg":message,"users":users}
    return jsonify(retdata)

@app.route('/editusersaveform',methods=['POST', 'GET'])
def posteditusersaveform():
    print("inside flask")
    msg = ""
    status = 1
    try:
        data = request.get_json()
        print(data)
        id = request.args.get('userid')
        user = User.query.get_or_404(id)
        checkuser = User.query.filter_by(username= data["name"]).first()
        if(checkuser):
            str1={"status":"fail"}
            msg = "username already exists"
        else:
            checkuser = User.query.filter_by(email= data["email"]).first()
            if(checkuser):
                status= 0
                msg = "email already exists"
            else:
                user.username= data["name"]
                user.email=data["email"]
                user.password=data["password"]
                db.session.commit()
                status= 1
                print("flask insde save users")
                msg="successfully done"
    except Exception as e:
            print(e)
            status= 0
            msg = "error found"
    str1={"status":status, "message": msg}
    print(msg)
    return str1

@app.route('/loginform',methods=['POST', 'GET'])
def loginform():
    users=[]
    message=""
    status=0
    try:
        data= request.get_json()
        checkusername = User.query.filter_by(username=data['username']).first()
        if(checkusername and checkusername.password==data['password']):
            login_user(checkusername)
            msg="user authenticated"
            status=1
        else:
            msg="invalid credentials"
            status=0
    except Exception as e:
            print(e)
            status=0
            msg="error found"
    str1={"status":status, "message": msg}
    print(msg)
    return jsonify(str1)

@app.route('/logoutform',methods=['POST', 'GET'])
def logoutform():
    msg=""
    status=0
    try:
        logout_user()
        msg="logged out successfully"
        status=1
    except Exception as e:
        print(e)
        status=0
        msg="error found"
    str1={"status":status, "message": msg}
    print(msg)
    return jsonify(str1)

@app.route('/searchuserform',methods=['POST', 'GET'])
def searchuserform():
    print("inside flask")
    users=[]
    msg = ""
    try:
        data= request.get_json()
        user = User.query.filter_by(username=data['name']).first()
        if(user):
            msg="user exists"
            dict = {"id":user.id,"name":user.username,"email":user.email,"password":user.password}
            users.append(dict)
        else:
            msg="user not found"
            users=[]
    except Exception as e:
            print(e)
            msg = "error found"
    str1={"msg":msg,"users":users}
    print(str1)
    return jsonify(str1)