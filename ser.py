from flask import Flask,render_template,request
app=Flask(__name__)



@app.route('/')
def hello():
        #return name
        return render_template('w.html')

@app.route('/submit',methods=['post','get'])
def new():
        with open('new.csv','a')as ex:
                data=request.form['pass']
                print(data)
        
        return 'sucessful'
