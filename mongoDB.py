# col = db["Car"]  
# doc = col.find_one() 
# print ("\nfind_one() result:", doc)
####################################
from flask.globals import session
from flask.helpers import url_for
import pymongo
from flask import Flask,jsonify,render_template,request,redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://admin:GFHsax21310@10.100.2.83:27017")  #ใส่username and passwd IP ของโหนด MongoDB
db = client["Ass1"]  #ชิ่อของDatabase

@app.route('/hello/')
def hello(name=None):
    if '_name' in session :
        name = db.db.users0
        users = name.find({})
        count = name.count({})
        
        return render_template('hello.html', namevalues = users , number = count)

    return redirect(url_for('hello'))

@app.route('/get/<string:_id>')
def get_userid(_id):
    if '_id' in session:
        user = db.db.users0
        users = user.find(
            {
                '_id': _id
            }
        )
    
        count = users.count()
        return render_template('hello.html', namevalues=users, number=count)
    
    return redirect(url_for('hello'))

@app.route('/get/job/<string:_price>')
def get_job(_price):
    if '_price' in session:
        user = db.db.users0
        users = user.find(
            {
                '_price': _price
            }
        )

        count = users.count()
        return render_template('hello.html', namevalues=users, number=count)

    return redirect(url_for('hello'))

@app.route('/get/name/<string:_name>')
def get_name(_name):
    if '_name' in session:
        user = db.db.users0
        users = user.find(
            {
                '_name': _name
            }
        )

        count = users.count()
        return render_template('hello.html', namevalues=users, number=count)

    return redirect(url_for('hello'))
    
@app.route("/") #เช็คว่า Conect ได้หรือป่าว
def index(): 
    texts = "Hello World"
    return texts

#ดูข้อมูลใน Database ทั้งหมด
@app.route("/Car", methods=['GET'])
def get_allCar():
    char = db.Car #เป็นเหมือนการนำค่าชื่อหัวตารางมาใส่ในตัวแปร char
    output = []
    for x in char.find(): #ทำตามฟังชั่น
        output.append({'_name' : x['_name'],'_model' : x['_model'],
                        '_price' : x['_price']}) #เอาค่าในตารางมาอ่านแล้วใส่ไปใน output เป็นเหมือนค่าอาเร
    return jsonify(output) #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ดูข้อมูลแบบทีละหัวข้อโดยใช้ชื่อของข้อมูล
@app.route("/Car/<name>", methods=['GET'])
def get_oneCar(name):
    char = db.Car #เป็นเหมือนการนำค่าชื่อหัวตารางมาใส่ในตัวแปร char
    x = char.find_one({'_name' : name}) #ชื่อข้อมูลที่จะหามาใส่ค่า name
    if x:
        output = ({'_name' : x['_name'],'_model' : x['_model'],
                    '_price' : x['_price']})  #เอาค่าในตารางมาอ่านแล้วใส่ไปใน output เป็นเหมือนค่าอาเร
    else: #หากหาไฟล์ไม่ครบหรือพิมชื่อผิดจะทำการแสดงข้อความ
         output = "No such name"
    return jsonify(output) #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ทำการ insert ข้อมูลตารางเข้าไปใหม่
@app.route('/Car', methods=['POST'])
def add_postcar():
  char = db.Car
  name = request.json['_name'] #ทำการสร้างตัวแปรใหม่เพื่อรับค่าจาก _name
  model = request.json['_model']
  price = request.json['_price']
  
  char_id = char.insert({'_name': name, #ทำการพิมให้ตรงกับชื่อตารางแล้วกด sent จะทำการไปทำการทำงานในบรรทัดที่ 53
                        '_model': model,
                        '_price': price,})
  new_char = char.find_one({'_id': char_id }) #สร้างIP ขึ้นมาใหม่โดยการสุ่ม
  output = {'_name' : new_char['_name'], #หลังจากสร้างเพิ่มแล้วทำการใส่เข้าไปในตัวแปรที่สร้างมาทำการใส่ค่าลง output
                        '_model' : new_char['_model'],
                        '_price' : new_char['_price'],}
  return jsonify(output)  #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ทำการ edit ข้อมูลตารางโดยการอิง name or _name
@app.route('/Car/<name>', methods=['PUT'])
def update_character(name):
    char = db.Car
    x = char.find_one({'_name' : name}) #เอาค่าที่ใส่มาใน name เพื่อเช็คว่าตรงกับตารางไหน
    if x: #ในตัวแปร x มี name ที่เรากรอกลงไปใน /Car/<name>
        myquery = {'_name' : x['_name'], #เรียกข้อมูลมาใส่ใน myquery
                        '_model' : x['_model'],
                        '_price' : x['_price']}

    name = request.json['_name'] #ทำการสร้างตัวแปรใหม่เพื่อรับค่าจาก _name
    model = request.json['_model']
    price = request.json['_price']
    
    newvalues = {"$set" : {'_name' : name,  #ทำการแก้ไขไฟล์แล้วใส่ไปในตัวแปรที่ส้รางรวมกันเป็นอาเร
                        '_model': model,
                        '_price': price,}}
    char_id = char.update_one(myquery, newvalues) #ส่งไปอัพเดท
    output = {'_name' : name,  #นำค่าที่อัพเดทมาทั้งหมดลงตัวแปร output
                        '_model': model,
                        '_price': price,}
    return jsonify(output) #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ทำการ Deleted ข้อมูลตารางโดยการอิง name or _name
@app.route('/Car/<name>', methods=['DELETE'])
def Car_delete(name):
    char = db.Car
    x = char.find_one({'_name' : name}) #ในตัวแปร x มี name ที่เรากรอกลงไปใน /Car/<name>

    char_id = char.delete_one(x) #นำ x มาทำฟังชัั่น delete_one 

    output = "Deleted complete" # หลังจากลบเสร็จแสดงข้อความ

    return jsonify(output) #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ตัว Run server
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 80)