from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "biotoilet-krasnoyarsk-2026")

# Примерные цены (можно легко менять)
PRICES = {
    "standard": {"name": "Стандартный биотуалет", "price": 4500, "desc": "Для стройки, мероприятий, дачи"},
    "comfort": {"name": "Комфорт (с раковиной)", "price": 6500, "desc": "Улучшенный, для более длительной аренды"},
    "vip": {"name": "VIP / Для мероприятий", "price": 9500, "desc": "Красивый, с освещением и дополнительными удобствами"},
}

@app.route("/")
def index():
    return render_template("index.html", prices=PRICES)

@app.route("/order", methods=["POST"])
def order():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    model = request.form.get("model", "")
    days = request.form.get("days", "1")
    comment = request.form.get("comment", "").strip()

    if not name or not phone:
        flash("Пожалуйста, укажите имя и телефон", "error")
        return redirect(url_for("index"))

    # Здесь в реальном проекте можно отправлять в Telegram, на почту или в CRM
    print(f"=== НОВАЯ ЗАЯВКА ===")
    print(f"Имя: {name}")
    print(f"Телефон: {phone}")
    print(f"Модель: {model}")
    print(f"Дней: {days}")
    print(f"Комментарий: {comment}")
    print("====================")

    flash(f"Спасибо, {name}! Мы свяжемся с вами по номеру {phone} в ближайшее время.", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
