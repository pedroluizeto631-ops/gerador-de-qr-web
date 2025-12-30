from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None

    if request.method == "POST":
        texto = request.form["texto"]

        img = qrcode.make(texto)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        imagem_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        qr_image = f"data:image/png;base64,{imagem_base64}"

    return render_template("index.html", qr=qr_image)

if __name__ == "__main__":
    app.run()
