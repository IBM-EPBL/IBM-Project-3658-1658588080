from flask import Flask, render_template, request
app = Flask( name )
@app.route('/')
def student():
    return render_template('index.html')


if  __name__=='__main__':
    app.run(debug = True)
