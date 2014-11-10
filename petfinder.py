import json, urllib2

url = "http://api.petfinder.com/auth.getToken?key=0d8229854a6b11ffdbcbe87548b21c1b&sig=daae400291deb160215612dd7e1c025d"
request = urllib2.urlopen(url)
result = request.read()
print result
