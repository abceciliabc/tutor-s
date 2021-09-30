from flask import Flask, render_template
app = Flask(__name__)

## HTML 화면 보여주기
@app.route('/')
def travel():
    return render_template('index.html')

@app.route('/menu1')
def record():
    return render_template('write.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

