from flask import Flask, render_template, request, redirect, url_for, session
import random
import string
ksa = string.ascii_lowercase + string.digits
jor = ''.join(random.choice(ksa) for i in range(7))
app = Flask(__name__)
ss = '''
 @import url('https://fonts.googleapis.com/css2?family=Tajawal&display=swap');
            body {
                margin: 0px;
                padding: 0px;
                font-family: 'Tajawal', sans-serif;
                background-size: cover;
                background-color: #151c22;
            }
            
            .snap {
                width: 250px;
                height: 80px;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-wrap: wrap;
                box-shadow: 1px 1px 15px rgba(8, 8, 8, 0.452);
                background-color: yellow;
                margin: 20px;
                border-radius: 5px;
                overflow: hidden;
            }'''
app.secret_key = 'hello'
@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        user = request.form['nm']
        session['user'] = user
        snap = request.form['snap']
        session['snap'] = snap
        tek = request.form['tek']
        session['tek'] = tek
        tube = request.form['tube']
        session['tube'] = tube
        insta = request.form['insta']
        session['insta'] = insta
        dis = request.form['dis']
        session['dis'] = dis
        return redirect(url_for('user'))
    else:
        return render_template('home.html')
@app.route(f'/{jor}')
def user():
    if 'user' in session:
        user = session['user']
        snap = session['snap']
        tek = session['tek']
        tube = session['tube']
        insta = session['insta']
        dis = session['dis']
        return f"""
            <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome</title>
        </head>
        <br><br><br><br><br>
        <style>{ss}</style>

        <body>
            <center>
                <!--Snap-->
                <div class="snap">
                    <a href="{snap}"><img width="70px " src="https://www.designbust.com/download/637/png/snapchat_logo_png512.png "></a>
                    <h3 style="color: black; ">snap</h3>
                </div>
                <!--Tiktok-->
                <div class="snap" style="background-color: black;">
                    <a href="{tek}"><img width="50px " src="https://i.pinimg.com/originals/5d/d2/53/5dd25319e5ab4d5221bbc7da5e8a3bfa.png "></a>
                    <h3 style="color: white; ">Tiktok</h3>
                </div>
                <!--youtube-->
                <div class="snap" style="background-color: red;">
                    <a href="{tube}"><img width="90px " src="https://www.freepnglogos.com/uploads/youtube-logo-png-images-0.png "></a>
                    <h3 style="color: white; ">youtube</h3>
                </div>
                <div class="snap" style="background-color: rgb(179, 0, 170);">
                    <a href="{insta}"><img width="60px " src="https://www.freepnglogos.com/uploads/instagram-logo-png-transparent-0.png "></a>
                    <h3 style="color: white; ">instagram</h3>
                </div>
                <div class="snap" style="background-color: rgb(0, 128, 179);">
                    <a href="{dis}"><img width="60px " src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Telegram_Messenger.png/768px-Telegram_Messenger.png "></a>
                    <h3 style="color: whitesmoke; ">telegram</h3>
                </div>
                <h3 style="color : white">WELCOME {user}</h3>
                <h3 style="color : white">Your URL ->> {jor}</h3>
            </center>
        </body>

        </html>"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)
