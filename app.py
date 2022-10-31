#ec2-password
from flask import Flask, render_template, request
import math, ast

app = Flask(__name__)

class MyMath():

    def __init__(self) -> None:
        self.num_list = []
    
    def average(self) -> float:
        sum = 0
        count = 0

        for i in self.num_list:
            sum = sum + float(i)
            count = count + 1

        return (sum / count)

    def stddev(self) -> float:
        step2 = []
        step3 = 0.0
        sum = 0
        count = 0
        for i in self.num_list:
            sum = sum + float(i)
            count = count + 1
    
        mean = (sum / count)

        for i in self.num_list:
            j = pow((i - mean),2)
            step2.append(j)
    
        for k in step2:
            step3 += k
        sd = math.sqrt(step3 / count)
   
        return sd


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=('GET','POST'))
def result():
    if request.method == 'POST':
        MMObj = MyMath()
        MMObj.num_list = ast.literal_eval("[" + request.form['numlist'] + "]")
        #MMObj.num_list = [1,2,3,4,5,6,7,8,9,10]
        #print(MMObj.num_list)
        return render_template('result.html',numlist=MMObj.num_list, max=max(MMObj.num_list),average=MMObj.average(),stddev=MMObj.stddev())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
