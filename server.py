from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key='Spaghetti'
goButton = "<input class='btn-primary btn-lg' type='submit' value='Go >>>'>"
win = False

# start routes
@app.route('/')
def main():
    return render_template('index.html', z=goButton)

@app.route('/result', methods=['POST'])
def runNumber():
    session['number'] = request.form['pick']
    print(session)
    if 'cpuNum' not in session:
        session['cpuNum'] = random.randint(1,100)
    print(session['cpuNum'])
    resession = "<input class='btn-primary btn-lg' type='submit' value='Play Again'>"
    if session['cpuNum'] > int(request.form['pick']):
        return render_template('index.html', result='Too Low, You Slow!', clash='lose', z=goButton)
    if session['cpuNum'] < int(request.form['pick']):
        return render_template('index.html', result='Too High, Nice Try!', clash='lose', z=goButton)
    if session['cpuNum'] == int(request.form['pick']):
        win = True
        return render_template('index.html', result='You Win, Big Grin!', winNum='The Number is '+str(session['cpuNum']), clash='win', x=resession)

@app.route('/reset', methods=['POST'])
def resetSession():
    session.clear()
    return redirect('/')
# end rputes
if __name__=='__main__':
    app.run(debug=True)