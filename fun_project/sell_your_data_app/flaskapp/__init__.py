from flask import Flask, g, Response ,make_response, render_template


app = Flask(__name__)
app.debug = True

@app.route('/res1')
def res1():
    custom_res = Response('Custom Response', 200, {'test':'ttt'})
    return make_response(custom_res)


#WSGI(Webserver Gateway Interface)

@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'the request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type', 'text/plain'),('Content-Length', str(len(body)))]
        start_response('200 ok', headers)
        return[body]
    return make_response(application)


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'yeonghwan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)