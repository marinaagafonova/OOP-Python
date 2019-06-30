from flask import Flask, render_template, request, redirect, url_for
from search import Search

app = Flask(__name__)
# text = ''

@app.route('/', methods=['POST', 'GET'])
def index():
    # output = text
    output = read_from_file()
    if request.method == 'POST':
        if request.form['submit'] == 'Search':
            output = search(request.form['key'])
        elif request.form['submit'] == 'Edit':
            return render_template('edit.html', text=output)
        elif request.form['submit'] == 'Load':
            file = request.files['data_file']
            file_contents = file.stream.read().decode("utf-8")
            write_in_file(file_contents)
            output = read_from_file()

    return render_template('index.html', text=output)


@app.route('/edittext', methods=['POST'])
def editpost():
    # global text
    # text = request.form['content']
    write_in_file(request.form['content'])
    return redirect(url_for('index'))

def search(key):
    return Search.color_find(key, read_from_file(), True)

def read_from_file():
    output = ""
    with open("text.txt", 'r') as inf:
        for string in inf:
            output += string
    return output

def write_in_file(input):
    with open("text.txt", 'w') as ouf:
        ouf.truncate(0)
        ouf.write(input)


if __name__ == '__main__':
    app.run(debug=True)
