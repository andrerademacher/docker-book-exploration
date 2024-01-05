#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Template
import os, datetime


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        load = os.getloadavg()[0]
        time = datetime.datetime.now().astimezone()

        with open('/src/template.j2') as f:
            rendered = Template(f.read()).render(load=load, time=time)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(rendered, 'utf8'))
        return


def run():
    addr = ('', 8080)
    httpd = HTTPServer(addr, HelloWorldHandler)
    httpd.serve_forever()


run()