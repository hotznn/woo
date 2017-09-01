import ssl
import urllib2

def get(url):
  return urllib2.urlopen(url, context=ssl._create_unverified_context()).read()

def post(url, data):
  request = urllib2.Request(url, data) 
  return urllib2.urlopen(request, context=ssl._create_unverified_context()).read()