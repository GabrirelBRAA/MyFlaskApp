import os
from flask import Flask, render_template, redirect, url_for, session, send_file
from werkzeug.utils import secure_filename
from Misc.functions import * 
from flask import request

from Models.DB import DBConnection
from Models.Users_Controller import UserController

database = DBConnection("myFlaskApp", "postgres", "123", "127.0.0.1", "5432")
users = UserController(database)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)
app.secret_key = '#$ab9&^BB00_.'

@app.route("/")
def hello_world():
   return render_template("homepage.html")

@app.get("/login")
def login_get():
   return render_template("login.html")

@app.post("/login")
def login_post():
   result = users.request_name(request.form['fname'])
   if(result):
      result = result[0] #o resultado vem em uma lista (posso alterar isso dentro da função)
      if(hash(request.form['fpassword'], result[3]) == result[4]):
         session['username'] = request.form['fname']
         for file in os.listdir("images/" + request.form['fname']):
            if file.rsplit('.', 1)[0] == request.form['fname']:
               session['profile_image'] = file
         return redirect(url_for('hello_world'))
         
   return render_template("login.html")

@app.route("/logoff")
def logoff():
   session.pop('username', None)
   session.pop('profile_image', None)
   return redirect(url_for("hello_world"))

@app.route("/profile")
def profile():
   if 'username' not in session:
      return redirect(url_for('hello_world'))
   else: return render_template('profile.html')

@app.get("/sign")
def sign_get():
   return render_template("signup.html")

#Função de login bem complexa, posso tentar diminuir em algumas outras
@app.post("/sign")
def sign_post(): 
   errors = []
   if(users.request_name(request.form['fname'])):
      errors.append("Username already exists")
   if(request.form['fpassword'] != request.form['fconfirm']):
      errors.append("Passwords do not match")
   if(errors):
      return render_template("signup.html", errors = errors)
   path = "images/" + request.form['fname'] #The use image folder is created even if there is no image
   if(not os.path.isdir(path)):
      os.mkdir(path)
   file = request.files['file']
   if(file.filename != '' and allowed_file(file.filename, ALLOWED_EXTENSIONS)):#if image is correct, save it.
      filename = secure_filename(file.filename)
      file.save(path + "/" + request.form['fname'] + '.' + filename.rsplit('.', 1)[1].lower())
   #Agora e so atualizar o banco de dados
   salt = get_salt()
   pass_hash = hash(request.form['fpassword'], salt) #hash retorna uma lista com salt em segundo e password em primeiro
   parameters = [0, salt, pass_hash, request.form['fname']]
   users.insert(parameters) 
   return redirect(url_for('hello_world'))

@app.route("/images/<path:filename>")
def images(filename):
   separated_filename = filename.rsplit('.',1)
   return send_file("./images/" + separated_filename[0] + "/" + filename, mimetype = "image/" + separated_filename[1])







   
   
   
   
   
