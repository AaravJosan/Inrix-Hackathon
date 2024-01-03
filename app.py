from flask import Flask, render_template, request
import folium
from testMap import m
from getLat import runFunction

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def index():
    map_path = './templates/mymap.html'
    m.save(map_path)
    user_input1 = None
    user_input2 = None
    if request.method == 'POST':
        user_input1 = request.form['user_input1']
        user_input2 = request.form['user_input2']
        map_path = './templates/mymap.html'
        runFunction(user_input1, user_input2)
        m.save(map_path)
        return render_template('index.html', map_path = map_path,user_input1 = user_input1, user_input2 = user_input2)
    return render_template('index.html', map_path = map_path, user_input1 = user_input1, user_input2 = user_input2)

if __name__ == '__main__':
    app.run(debug=True)