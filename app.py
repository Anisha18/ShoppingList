from flask import Flask, request, jsonify

app=Flask(__name__)

shopping_list=[{
                    "id":0,
                    "product_name":"Saree",
                    "price":2900,
                    "color":"Blue",
                    "size":"NA"
                },
                {
                    "id":1,
                    "product_name":"Saree",
                    "price":3300,
                    "color":"Red",
                    "size":"NA"

                },
                {
                    "id":2,
                    "product_name":"Saree",
                    "price":4500,
                    "color":"Green",
                    "size":"NA"

                },
                {   
                    "id":3,
                    "product_name":"Kurtha",
                    "price":500,
                    "color":"Purple",
                    "size":"S",
                },
                {
                    "id":4,
                    "product_name":"Kurtha",
                    "price":799,
                    "color":"Yellow",
                    "size":"M",
                },
                {
                    "id":5,
                    "product_name":"Kurtha",
                    "price":999,
                    "color":"Pink",
                    "size":"M",
                },
                {
                    "id":6,
                    "product_name":"Top",
                    "price":1079,
                    "color":"Gray",
                    "size":"M",
                },
                {
                    "id":7,
                    "product_name":"Top",
                    "price":850,
                    "color":"Black",
                    "size":"S",
                },
                {
                    "id":8,
                    "product_name":"Jeans",
                    "price":1300,
                    "color":"Black",
                    "size":"M",
                },
                {
                    "id":9,
                    "product_name":"Jeans",
                    "price":900,
                    "color":"Blue",
                    "size":"S",
                },
                {
                    "id":10,
                    "product_name":"Shirt",
                    "price":789,
                    "color":"Blue",
                    "size":"M",
                },
                {
                    "id":11,
                    "product_name":"Shirt",
                    "price":650,
                    "color":"Maroon",
                    "size":"M",
                },
                {
                    "id":12,
                    "product_name":"T-Shirt",
                    "price":450,
                    "color":"Black",
                    "size":"M",
                },
                {
                    "id":13,
                    "product_name":"T-Shirt",
                    "price":729,
                    "color":"Green",
                    "size":"S",
                },
                {
                    "id":14,
                    "product_name":"Trouser",
                    "price":1200,
                    "color":"Gray",
                    "size":"M",
                },
                {
                    "id":15,
                    "product_name":"Trouser",
                    "price":1100,
                    "color":"Brown",
                    "size":"M",
                }]
            

@app.route('/shopping',methods=['GET', 'POST'])
def shopping():
    if request.method == 'GET':
        if len(shopping_list) > 0:
            return jsonify(shopping_list)
        else:
            'Nothing Found',404
    if request.method == 'POST':
        new_product = request.form['product_name']
        new_price = request.form['price']
        new_color = request.form['color']
        new_size = request.form['size']
        iD=shopping_list[-1]['id']+1

        new_obj={
            'id':iD,
            'product_name':new_product,
            'price':new_price,
            'size':new_size,
            'color':new_color,
        }
        shopping_list.append(new_obj)
        return jsonify(shopping_list), 201

@app.route('/shopping/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_item(id):
    if request.method == 'GET':
        for item in shopping_list:
            if item['id'] == id:
                return jsonify(item)
            pass
    if request.method == 'PUT':
        for item in shopping_list:
            if item['id'] == id:
                item['product_name'] = request.form['product_name']
                item['price'] = request.form['price']
                item['color'] = request.form['color']
                item['size'] = request.form['size']
                updated_item = {
                        'id': id,
                        'product_name': item['product_name'],
                        'price': item['price'],
                        'color': item['color'],
                        'size': item['size']
                }
                return jsonify(updated_item)
    if request.method == 'DELETE':
        for index, item in enumerate(shopping_list):
            if item['id'] == id:
                shopping_list.pop(index)
                return jsonify(shopping_list)


if __name__ == '__main__':
    app.run()
















