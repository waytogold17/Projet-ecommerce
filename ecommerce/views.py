from flask import Flask, render_template
from flask import flash, g, redirect, render_template, request, session, url_for
from .config import app,db
from .models import Client




def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Fastbase.db'
    db.init_app(app)
    from . import views
    @app.route('/')
    def  index():
        return render_template("accueil.html")
    
    @app.route('/hello')
    def hello():
                return 'Hello, World!'
    @app.route('/inscription/')
    def accueil():
        return render_template("auth/inscription.html")
    @app.route('/inscription/inscription/')
    def accueil10():
        return render_template("auth/inscription.html")
    
    @app.route('/inscription/connexion/connexion/')
    def lasortie():
        return render_template("auth/connexion.html")
    
    
    @app.route('/inscription/connexion/')
    def retourinscription():
        return render_template("auth/connexion.html")
    
    
    
            
    @app.route('/inscription/session/inscription/')
    def accueil3():
        return render_template("auth/inscription.html")
    
    @app.route('/inscription/auth',methods=["POST"])
    def insertion():
        if request.method == 'POST':
            nom = request.form['nom']
            prenom = request.form['prenom']
            email = request.form['email']
            password = request.form.get("pw1")
            confirm_password = request.form.get("pw2")
            registered_users = {
            "utilisateur1",
            "utilisateur2",
            "utilisateur3"
            }
            # Vérification si le nom d'utilisateur est déjà enregistré
            if nom in registered_users:
                    return "Le nom d'utilisateur est déjà pris."
            else:
                    registered_users.add(nom)
                    
            if password != confirm_password:
                return "Les mots de passe ne correspondent pas."
            
            else:
                def register_user(nom, password, users):
                    users[nom] = password
                    return users

                global users
                users = {}
                users = register_user(nom, password, users)
                client = Client(nom=nom,prenom=prenom, email=email)
                db.session.add(client)
                db.session.commit()
                return render_template("accueil.html")
                redirect(render_template("auth/session.html"))
    
    @app.route('/inscription/connexion/auth',methods=["POST"])
    def laconnec2():
        if request.method == "POST":
            nom = request.form.get("nom")
            password = request.form.get("password")
        
               
            # Vérification si le nom d'utilisateur et le mot de passe existent dans le dictionnaire
            if nom in users and users[nom] == password:
                return render_template("auth/session.html")
            else:
                return "Echec de la connexion"
    
    @app.route('/connexion/auth',methods=["POST"])
    def register():
        if request.method == "POST":
            nom = request.form.get("nom")
            password = request.form.get("password")
        
            if nom in users and users[nom] == password:
                return render_template("auth/session.html")
            else:
                return "Echec de la connexion"
        
            
                
        else:
            redirect("/connexion/") 
    
    @app.route('/connexion/')
    def connexion():
        return render_template("auth/connexion.html")
    
    
    @app.route('/connexion/auth/session/')
    def laconnec():
        return render_template("auth/session.html")
    
    @app.route('/inscription/session/connexion/')
    def connexion3():
        return render_template("auth/connexion.html")
    
    @app.route('/session/')
    def session():
        return render_template("auth/session.html")
    
    @app.route('/inscription/session/')
    def session2():
        return render_template("auth/session.html")
    
    @app.route('/connexion/session/')
    def session3():
        return render_template("auth/session.html")
    
    return app
 
    
   
     

