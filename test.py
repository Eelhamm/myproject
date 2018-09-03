from flask import Flask,request
app=Flask(__name__)
#@app.route("/fill form",methods=['post','get'])
#def form():
 #   return render_template('test.html')
#if __name__ == "__main__":
   # app.run(host='127.0.0.1', port=800, debug=True)



@app.route("/fill form",methods=['post','get'])
def fill_form():
    firstname = Request.values.get('first name')
    lastname = Request.values.get('lastname')
    password = Request.values.get('password')
    if Request.methods=='get':
        return ('firstname')