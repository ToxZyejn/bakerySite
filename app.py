from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Товары пекарни
products = [
    {'id': 1, 'name': 'Хлеб', 'price': 30},
    {'id': 2, 'name': 'Булочка', 'price': 20},
    {'id': 3, 'name': 'Пирог', 'price': 100},
    {'id': 4, 'name': 'Кекс', 'price': 50},
    {'id': 5, 'name': 'Печенье', 'price': 15},
    {'id': 6, 'name': 'Рогалик', 'price': 25},
    {'id': 7, 'name': 'Торт', 'price': 200},
    {'id': 8, 'name': 'Пончик', 'price': 40},
    {'id': 9, 'name': 'Круассан', 'price': 60},
    {'id': 10, 'name': 'Маффин', 'price': 35}
]

cart = {}

@app.route('/')
def index():
    return render_template('index.html', products=products)

#функция использует REST метод POST для добавления товара в корзину
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        product = next((item for item in products if item['id'] == product_id), None)
        if product:
            cart[product_id] = {'name': product['name'], 'price': product['price'], 'quantity': quantity}
    return redirect(url_for('index'))

# этот путь переводит нас в корзину и считает итоговую сумму всех товаров
@app.route('/cart')
def show_cart():
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_price=total_price)

#запуск локального сервера с открытие сайта. Порт можно поменять на необходимый
if __name__ == '__main__':
    app.run(debug=True, port=8080)
