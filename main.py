from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

items = ["item1","item2","item3","item4","item5",]

@app.route("/index")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/mostrar_ip"))
    response.set_cookie("tu_ip", user_ip)  # Asegúrate de que la cookie se establece antes de redirigir
    return response

@app.route("/mostrar_ip")
def show_information():
    user_ip = request.cookies.get("tu_ip")
    context = {
        "user_ip" : user_ip,
        "items" : items
    }
    return render_template("index.html", **context)

app.run(host='0.0.0.0', port=8080, debug=True)
