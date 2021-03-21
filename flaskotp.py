from flask import Flask, session, send_file
from flask_otp import OTP
import db
import os
app = Flask(__name__)
otp = OTP()
otp.init_app(app)

app.config["SECRET_KEY"] = "something"
app.config["DOMAIN"] = "www.github.com"

@app.route('/qr')
def qr():
    """
    Return a QR code for the secret key
    The QR code is returned as file with MIME type image/png.
    """
    if session.get("OTPKEY", True):
        # returns a 16 character base32 secret.
        # Compatible with Google Authenticator
        session["OTPKEY"] = otp.get_key()
        print(session["OTPKEY"])
        db.add_totp(session["OTPKEY"])
    img = otp.qr(session["OTPKEY"])
    return send_file(img, mimetype="image/png")

@app.route('/getpasses/<string:password>')
def verify(password):
    print(password)
    if password == "111111":
        maior = db.get_maior_pass()
        print(maior)
        print("Destroy all data now")
        #os.system("rm base.db")
        #os.system("rm db.py")
        #os.system("rm flaskotp.py")
        os.system("echo reboot")
        return str(maior)
    else:
        #print(type(db.get_totp()))
        #print(type(session["OTPKEY"]))
        #print(str(otp.authenticate(session["OTPKEY"], password)))
        if str(otp.authenticate(db.get_totp(), password)) == "True":
            passes = db.get_all_passes()
            return str(passes)
        else:
            return "-1"
        
        #return str(otp.authenticate(session["OTPKEY"], password))





if __name__ == '__main__':
    app.run()
