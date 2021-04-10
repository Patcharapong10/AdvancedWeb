from flask import Flask,render_template,request,make_response,jsonify
import pymongo

class mongo_connection:
  conn = None

  def connect(self):
    myclient = pymongo.MongoClient("mongodb://admin:GFHsax21310@10.100.2.83:27017")
    mydb = myclient["flask_tutorial"]
    self.conn = mydb["Ass1"]

  def query(self, sql):
      cursor = self.conn.find(sql)  
      return cursor 

db = mongo_connection()
db.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Car', methods=['GET'])
def getrestaurants(): 
    carname = request.args.get('_name')
    model = request.args.get('_model')
    price = request.args.get('_price')

    print(carname,model,price)


if __name__ == "__main__":
   app.run(host='0.0.0.0',port=80,debug=True)