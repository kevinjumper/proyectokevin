from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route("/index")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/mostrar_ip"))
    response.set_cookie("tu_ip", user_ip)  # Asegúrate de que la cookie se establece antes de redirigir
    return response

@app.route("/mostrar_ip")
def show_information():
    user_ip = request.cookies.get("tu_ip")
    return f"klk mio, es esta tu ip?: {user_ip}"



app.run(host='0.0.0.0', port=8080, debug=True)
