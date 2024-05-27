from werkzeug.wrappers import Request, Response

# add function to tell the server to run any request code coming from our browser 
@ Request.application
def application(request):
    print (f'This web server  is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

#Running the server 
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname = 'localhost',
        port = 5555,
        application = application
    )
    
   


