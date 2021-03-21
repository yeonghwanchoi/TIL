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

# @app.before_request
# def before_request():
#     return None

# @app.route("/gg")
# def hahaha():
#     return "안녕 세계" + getattr(g, 'str', '111')

# @app.after_request
# def after_request():
#     return None 

@app.route("/")
@app.route("/index")
def index():
    user = {'username':"yeonghwan"} 
    return render_template('index.html', title='blog',user=user)
# @app.teardown_request
# def distroy_transaction():
#     return None
# @app.route('/sd')
# def helloworld_local():
#     return "hahah"

# @app.route('/sd', subdomain='g')
# def helloworld_local():
#     return "hahah"