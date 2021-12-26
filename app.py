from flask import Flask, render_template, request

# 1. Config static folder and template folder into one file is ./templates
# Find solution at here: https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask

app = Flask(__name__, static_url_path='',
            static_folder='templates',
            template_folder='templates')

# Home Page:
@app.route('/')
def rootRoute():
    # return render_template('khaibaoyte.html')
    return render_template('dashboard.html')

# Dashboard Page:
@app.route('/dashboard')
def dashboardRoute():
    return render_template('dashboard.html')

# Update Page:
@app.route('/update')
def updateRoute():
    return render_template('khaibaoyte.html')

# GioiThieu Page:
@app.route('/gioithieu')
def IntroRoute():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
