#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from twisted.web import resource, server
from twisted.internet import reactor, endpoints

class HttpRequestHandler(resource.Resource):
    isLeaf = True
    resources = {}

    def __init__(self, resources):
        self.resources = resources

    def render_GET(self, request):

        if self.resources.has_key(request.path):
           request.setResponseCode(200)
           content = self.resources[request.path]['html']
        else:
           request.setResponseCode(404)
           content = self.resources['not_found']['html']

        request.setHeader('Content-Type', 'text/html')
        return content.encode("ascii")

class HttpServer:
  port = '8008'
  resources = {
    'not_found': {'html': "<h1>Not Found</h1>Sorry, no such resource."}, 
    '/': {'html': '<h1>There you go</h1>The server is running even without any config'},
  }
  
  def __init__(self, port, resources):
    self.port = port
    self.resources = resources

  def run(self):
    port = 'tcp:' + self.port
    endpoints.serverFromString(reactor, port).listen(server.Site(HttpRequestHandler(self.resources)))
    reactor.run()