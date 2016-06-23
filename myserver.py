#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from http import HttpServer

resources = {
	'not_found': {'html': "<h1>Not Found</h1>Sorry, no such resource."}, 
	'/': {'html': '<h1>Home</h1>Home page'}, 
	'/about': {'html':'<h1>About</h1>All about me'},
	'/bunny': {'html': 'My html new'},
}

s = HttpServer('8030', resources)
s.run()
