#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
import json                                                                      
import datetime

def cnt():
    cnt.i += 1
    return cnt.i

cnt.i=0

class RequestHandler(BaseHTTPRequestHandler):


    
    def do_GET(self):
        request_path = self.path
        print("\n----- Request Start ----->\n")
        print(request_path)
        print(self.headers)
        print("<----- Request End -----\n")

        now = datetime.datetime.now()
        self.send_response(200)
        self.send_header('Content-type','text-html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()


        #send file content to client
        if (request_path.find("czas")!=-1):
                self.wfile.write(json.dumps({"godziny": now.hour, "minuty": now.minute, "sekundy": now.second}))
        else:
                self.wfile.write("Hello world")

    def do_POST(self):

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0

        print(request_headers)
        print(self.rfile.read(length))
        print("<----- Request End -----\n")

        self.send_response(200)

    do_PUT = do_POST
    do_DELETE = do_GET
    

def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()

    main()
