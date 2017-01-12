from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='ThisIsSecret'


@app.route('/')
def index():
    if not 'gold'in session:
        session['gold']=0
    if not 'result' in session:
        session['result']=0
    if not 'where' in session:
        session['where']='where'
    if not 'res' in session:
        session['res']=[]

    return render_template("gold.html")

@app.route('/process_money', methods=['POST'])
def makeMoney():
    if request.form['building']=='egypt':
        session['result']=0
        session['result']=session['result']+random.randrange(1, 6)
        session['gold']=session['gold']+session['result']
        session['where']='Egypt'
    elif request.form['building']=='cholula':
        session['result']=0
        session['result']=session['result']+random.randrange(-4, 11)
        session['gold']=session['gold']+session['result']
        session['where']='Cholula'
    elif request.form['building']=='atlantis':
        session['result']=0
        session['result']=session['result']+random.randrange(9, 21)
        session['gold']=session['gold']+session['result']
        session['where']='Atlantis'
    elif request.form['building']=='casino':
        session['result']=0
        session['result']=session['result']+random.randrange(-51, 51)
        session['gold']=session['gold']+session['result']
        session['where']='Casino'
    else:
        print 'Fuck you'
    respond()
    return redirect('/')
def respond():
    session['res'].append('You earned '+ str(session['result'])+ ' gold from the '+ str(session['where'])+'!')

    return redirect('/')






app.run(debug=True)
