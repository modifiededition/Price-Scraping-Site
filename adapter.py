
from flask import Flask, render_template, request
import web_crawler

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = None
    print( 1)
    if request.method == 'POST':
        query = request.form['search']
        print(query)
        result = web_crawler.main(query)
        print(result)
        if result is None:
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('first.html', error=error , result = result)        

    return render_template('first.html', error=error)

if __name__ == '__main__':
    app.run(debug = True)
