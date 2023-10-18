from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    

@app.route('/play')
def play():
    return render_template("index.html", times=3)	# notice the 2 new named arguments!

@app.route('/play/<int:times>')
def play2(times):
    return render_template("index.html",times=times)

@app.route('/play/<int:times>/<color>')
def play3(times,color):
    return render_template("index.html",times=times,color=color)


if __name__=="__main__":
    app.run(debug=True)                   

