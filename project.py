#!/usr/bin/env python2.7
import MySQLdb
import time
import urllib2
import json
#!time.time()

conn = MySQLdb.connect("","","","")

#<<<-------------------------------
#<<<-------------------------------LONDON------------------------------->>>
#------------------------------->>>

c = conn.cursor()
#LONDON TIME wunderground----------------------------------->>>
c.execute ("UPDATE london SET time= '%s' WHERE places='wundergrou'"%(time.time()))
#END LONDON TIME----------------------------------->>>

#LONDON TEMP wunderground----------------------------------->>>
try :
    f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/london.json')
    json_string = f.read()

    parsed_json = json.loads(json_string)

    location = parsed_json['location']['city']

    temp_f = parsed_json['current_observation']['temp_c']
    lontemp = temp_f
    print "Current temperature in %s is: %s" % (location, temp_f)

    f.close()
    print lontemp

    c.execute ("UPDATE london SET temp= '%s' WHERE places='wundergrou'"%(lontemp))

    conn.commit()
#END LONDON TEMP----------------------------------->>>

#LONDON HUM wunderground----------------------------------->>>
    f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/london.json')
    json_string = f.read()

    parsed_json = json.loads(json_string)

    location = parsed_json['location']['city']

    temp_f = parsed_json['current_observation']['relative_humidity']
    lonhum = temp_f
    lonhum = lonhum.replace("%", "")
    print "Current humidity in %s is: %s" % (location, temp_f)

    f.close()
    print lonhum

    c.execute ("UPDATE london SET hum= '%s' WHERE places='wundergrou'"%(lonhum))

    conn.commit()
#END LONDON HUM----------------------------------->>>

#LONDON windspeed wunderground----------------------------------->>>
    f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/london.json')
    json_string = f.read()

    parsed_json = json.loads(json_string)

    location = parsed_json['location']['city']

    temp_f = parsed_json['current_observation']['wind_mph']
    lonhum = temp_f
    print "Current windspeed(mph) in %s is: %s" % (location, temp_f)

    f.close()
    print lonhum

    c.execute ("UPDATE london SET windspeed= '%s' WHERE places='wundergrou'"%(lonhum))

    conn.commit()
except :
    pass
#END LONDON windspeed----------------------------------->>>


#LONDON TIME open weather----------------------------------->>>
c.execute ("UPDATE london SET time= '%s' WHERE places='openweathe'"%(time.time()))
#END LONDON TIME----------------------------------->>>

#LONDON TEMP openweather----------------------------------->>>
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=4cb8ed260c2d5f12750c5a5107b9eb70')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['temp']
lontemp = temp_f
lontemp = lontemp - 273 #because kelvin to cel =- 273
print "Current temperature in open weather%s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE london SET temp= '%s' WHERE places='openweathe'"%(lontemp))

conn.commit()
#END LONDON TEMP----------------------------------->>>

#LONDON HUM openweather----------------------------------->>>
#got rid of the declaring f and other
parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['humidity']
lonhum = temp_f
print "Current humidity open weather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE london SET hum= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END LONDON HUM----------------------------------->>>

#LONDON windspeed open weather----------------------------------->>>
#got rid of the declaring f and other

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['wind']['speed']
lonhum = temp_f
# conversion metres per sec to mph
lonhum = lonhum * 3600 # secs to hours
lonhum = lonhum / 1609.344 #metres to miles

print "Current windspeed(mph) openweather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE london SET windspeed= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END LONDON windspeed----------------------------------->>>

#LONDON TIME darkspy----------------------------------->>>
c.execute ("UPDATE london SET time= '%s' WHERE places='darksky'"%(time.time()))
#END LONDON TIME----------------------------------->>>

#LONDON TEMP darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/51.50722,-0.12750')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['temperature']
lontemp = temp_f
print "Current temperature darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp - 32 # convert to cel
lontemp = lontemp / 1.8
f.close()
print lontemp

c.execute ("UPDATE london SET temp= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LONDON TEMP----------------------------------->>>

#LONDON TIME darkspy----------------------------------->>>
c.execute ("UPDATE london SET time= '%s' WHERE places='darksky'"%(time.time()))
#END LONDON TIME----------------------------------->>>

#LONDON HUM darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/51.50722,-0.12750')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['humidity']
lontemp = temp_f
print "Current humidity darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp * 100
f.close()
print lontemp

c.execute ("UPDATE london SET hum= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LONDON TEMP----------------------------------->>>

#LONDON WINDSPEED darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/51.50722,-0.12750')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['windSpeed']
lontemp = temp_f
print "Current windspeed darksky in %s is: %s" % (location, temp_f)
f.close()
print lontemp

c.execute ("UPDATE london SET windspeed= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LONDON TEMP----------------------------------->>>

#LONDON TIME wunderground----------------------------------->>>
c.execute ("UPDATE london SET time= '%s' WHERE places='final'"%(time.time()))
#END LONDON TIME----------------------------------->>>

#LONDON TEMP averages----------------------------------->>>
c.execute("SELECT temp FROM london WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT temp FROM london WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT temp FROM london WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = int(t10)
t10 = t10 / 3
c.execute ("UPDATE london SET temp= '%s' WHERE places='final'"%(t10))
c.execute("SELECT temp FROM london ""WHERE places ='darksky'")
query = c.fetchone()
#END LONDON TEMP----------------------------------->>>

#LONDON HUM averages----------------------------------->>>
c.execute("SELECT hum FROM london WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT hum FROM london WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT hum FROM london WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE london SET hum= '%s' WHERE places='final'"%(t10))
#
#END LONDON HUM----------------------------------->>>

#LONDON WINSPEED averages----------------------------------->>>
c.execute("SELECT windspeed FROM london WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT windspeed FROM london WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT windspeed FROM london WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE london SET windspeed= '%s' WHERE places='final'"%(t10))
#
#END LONDON WINDSPEED----------------------------------->>>

#TESTING LONDON----------------------------------->>>
print "THESE ARE THE TESTS FOR LONDON"
print t1
print t10
print query

c.execute("SELECT * FROM london")
rows = c.fetchall()
for eachRow in rows:
    print eachRow
print "TEST FOR LONDON END"
#END OF TESTING--------------------------->>>

#<<<-------------------------------
#<<<-------------------------------MANCHESTER------------------------------->>>
#------------------------------->>>

#MANCHESTER TIME wunderground----------------------------------->>>
c.execute ("UPDATE manchester SET time= '%s' WHERE places='wundergrou'"%(time.time()))
#END MANCHESTER TIME----------------------------------->>>

#MANCHESTER TEMP wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/manchester.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_c']
lontemp = temp_f
print "Current temperature in %s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE manchester SET temp= '%s' WHERE places='wundergrou'"%(lontemp))

conn.commit()
#END MANCHESTER TEMP----------------------------------->>>

#MANCHESTER HUM wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/manchester.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['relative_humidity']
lonhum = temp_f
lonhum = lonhum.replace("%", "")
print "Current humidity in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE manchester SET hum= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END MANCHESTER HUM----------------------------------->>>

#MANCHESTER windspeed wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/manchester.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['wind_mph']
lonhum = temp_f
print "Current windspeed(mph) in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE manchester SET windspeed= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END MANCHESTER windspeed----------------------------------->>>

#MANCHESTER TIME open weather----------------------------------->>>
c.execute ("UPDATE manchester SET time= '%s' WHERE places='openweathe'"%(time.time()))
#END MANCHESTER TIME----------------------------------->>>

#MANCHESTER TEMP openweather----------------------------------->>>
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=manchester,uk&appid=4cb8ed260c2d5f12750c5a5107b9eb70')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['temp']
lontemp = temp_f
lontemp = lontemp - 273 #because kelvin to cel =- 273
print "Current temperature in open weather%s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE manchester SET temp= '%s' WHERE places='openweathe'"%(lontemp))

conn.commit()
#END MANCHESTER TEMP----------------------------------->>>

#MANCHESTER HUM openweather----------------------------------->>>
#got rid of the declaring f and other
parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['humidity']
lonhum = temp_f
print "Current humidity open weather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE manchester SET hum= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END MANCHESTER HUM----------------------------------->>>

#MANCHESTER windspeed open weather----------------------------------->>>
#got rid of the declaring f and other

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['wind']['speed']
lonhum = temp_f
# conversion metres per sec to mph
lonhum = lonhum * 3600 # secs to hours
lonhum = lonhum / 1609.344 #metres to miles

print "Current windspeed(mph) openweather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE manchester SET windspeed= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END MANCHESTER windspeed----------------------------------->>>

#MANCHESTER TIME darkspy----------------------------------->>>
c.execute ("UPDATE manchester SET time= '%s' WHERE places='darksky'"%(time.time()))
#END MANCHESTER TIME----------------------------------->>>

#MANCHESTER TEMP darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/53.483959,-2.244644')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['temperature']
lontemp = temp_f
print "Current temperature darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp - 32 # convert to cel
lontemp = lontemp / 1.8
f.close()
print lontemp

c.execute ("UPDATE manchester SET temp= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END MANCHESTER TEMP----------------------------------->>>

#MANCHESTER TIME darkspy----------------------------------->>>
c.execute ("UPDATE manchester SET time= '%s' WHERE places='darksky'"%(time.time()))
#END MANCHESTER TIME----------------------------------->>>

#MANCHESTER HUM darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/53.483959,-2.244644')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['humidity']
lontemp = temp_f
print "Current humidity darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp * 100
f.close()
print lontemp

c.execute ("UPDATE manchester SET hum= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END MANCHESTER TEMP----------------------------------->>>

#MANCHESTER WINDSPEED darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/53.483959,-2.244644')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['windSpeed']
lontemp = temp_f
print "Current windspeed darksky in %s is: %s" % (location, temp_f)
f.close()
print lontemp

c.execute ("UPDATE manchester SET windspeed= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END MANCHESTER TEMP----------------------------------->>>

#MANCHESTER TIME averages----------------------------------->>>
c.execute ("UPDATE manchester SET time= '%s' WHERE places='final'"%(time.time()))
conn.commit()
#END MANCHESTER TIME----------------------------------->>>

#MANCHESTER TEMP averages----------------------------------->>>
c.execute("SELECT temp FROM manchester WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT temp FROM manchester WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT temp FROM manchester WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE manchester SET temp= '%s' WHERE places='final'"%(t10))
conn.commit()
#END MANCHESTER TEMP----------------------------------->>>

#MANCHESTER HUM averages----------------------------------->>>
c.execute("SELECT hum FROM manchester WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT hum FROM manchester WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT hum FROM manchester WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE manchester SET hum= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END MANCHESTER HUM----------------------------------->>>

#MANCHESTER WINSPEED averages----------------------------------->>>
c.execute("SELECT windspeed FROM manchester WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT windspeed FROM manchester WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT windspeed FROM manchester WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE manchester SET windspeed= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END MANCHESTER WINDSPEED----------------------------------->>>

#TESTING MANCHESTER----------------------------------->>>
print "THESE ARE THE TESTS FOR MANCHESTER"
print t1
print t10
print query

c.execute("SELECT * FROM manchester")
rows = c.fetchall()
for eachRow in rows:
    print eachRow
print "TEST FOR MANCHESTER END"
#END OF TESTING--------------------------->>>

#<<<-------------------------------
#<<<-------------------------------LIVERPOOL------------------------------->>>
#------------------------------->>>

#LIVERPOOL TIME wunderground----------------------------------->>>
c.execute ("UPDATE liverpool SET time= '%s' WHERE places='wundergrou'"%(time.time()))
#END LIVERPOOL TIME----------------------------------->>>

#LIVERPOOL TEMP wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/liverpool.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_c']
lontemp = temp_f
print "Current temperature in %s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE liverpool SET temp= '%s' WHERE places='wundergrou'"%(lontemp))

conn.commit()
#END LIVERPOOL TEMP----------------------------------->>>

#LIVERPOOL HUM wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/liverpool.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['relative_humidity']
lonhum = temp_f
lonhum = lonhum.replace("%", "")
print "Current humidity in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE liverpool SET hum= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END LIVERPOOL HUM----------------------------------->>>

#LIVERPOOL windspeed wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/liverpool.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['wind_mph']
lonhum = temp_f
print "Current windspeed(mph) in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE liverpool SET windspeed= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END LIVERPOOL windspeed----------------------------------->>>

#LIVERPOOL TIME open weather----------------------------------->>>
c.execute ("UPDATE liverpool SET time= '%s' WHERE places='openweathe'"%(time.time()))
#END LIVERPOOL TIME----------------------------------->>>

#LIVERPOOL TEMP openweather----------------------------------->>>
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=liverpool,uk&appid=4cb8ed260c2d5f12750c5a5107b9eb70')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['temp']
lontemp = temp_f
lontemp = lontemp - 273 #because kelvin to cel =- 273
print "Current temperature in open weather%s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE liverpool SET temp= '%s' WHERE places='openweathe'"%(lontemp))

conn.commit()
#END LIVERPOOL TEMP----------------------------------->>>

#LIVERPOOL HUM openweather----------------------------------->>>
#got rid of the declaring f and other
parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['humidity']
lonhum = temp_f
print "Current humidity open weather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE liverpool SET hum= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END LIVERPOOL HUM----------------------------------->>>

#LIVERPOOL windspeed open weather----------------------------------->>>
#got rid of the declaring f and other

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['wind']['speed']
lonhum = temp_f
# conversion metres per sec to mph
lonhum = lonhum * 3600 # secs to hours
lonhum = lonhum / 1609.344 #metres to miles

print "Current windspeed(mph) openweather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE liverpool SET windspeed= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END LIVERPOOL windspeed----------------------------------->>>

#LIVERPOOL TIME darksky----------------------------------->>>
c.execute ("UPDATE liverpool SET time= '%s' WHERE places='darksky'"%(time.time()))
#END LIVERPOOL TIME----------------------------------->>>

#LIVERPOOL TEMP darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/53.408371,-2.991573')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['temperature']
lontemp = temp_f
print "Current temperature darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp - 32 # convert to cel
lontemp = lontemp / 1.8
f.close()
print lontemp

c.execute ("UPDATE liverpool SET temp= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LIVERPOOL TEMP----------------------------------->>>

#LIVERPOOL TIME darkspy----------------------------------->>>
c.execute ("UPDATE liverpool SET time= '%s' WHERE places='darksky'"%(time.time()))
#END LIVERPOOL TIME----------------------------------->>>

#LIVERPOOL HUM darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/53.408371,-2.991573')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['humidity']
lontemp = temp_f
print "Current humidity darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp * 100
f.close()
print lontemp

c.execute ("UPDATE liverpool SET hum= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LIVERPOOL TEMP----------------------------------->>>

#LIVERPOOL WINDSPEED darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/53.408371,-2.991573')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['windSpeed']
lontemp = temp_f
print "Current windspeed darksky in %s is: %s" % (location, temp_f)
f.close()
print lontemp

c.execute ("UPDATE liverpool SET windspeed= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LIVERPOOL TEMP----------------------------------->>>

#LIVERPOOL TIME averages----------------------------------->>>
c.execute ("UPDATE liverpool SET time= '%s' WHERE places='final'"%(time.time()))
conn.commit()
#END LIVERPOOL TIME----------------------------------->>>

#LIVERPOOL TEMP averages----------------------------------->>>
c.execute("SELECT temp FROM liverpool WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT temp FROM liverpool WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT temp FROM liverpool WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE liverpool SET temp= '%s' WHERE places='final'"%(t10))
conn.commit()
#END LIVERPOOL TEMP----------------------------------->>>

#LIVERPOOL HUM averages----------------------------------->>>
c.execute("SELECT hum FROM liverpool WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT hum FROM liverpool WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT hum FROM liverpool WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE liverpool SET hum= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END LIVERPOOL HUM----------------------------------->>>

#LIVERPOOL WINSPEED averages----------------------------------->>>
c.execute("SELECT windspeed FROM liverpool WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT windspeed FROM liverpool WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT windspeed FROM liverpool WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE liverpool SET windspeed= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END LIVERPOOL WINDSPEED----------------------------------->>>

#TESTING LIVERPOOLL----------------------------------->>>
print "THESE ARE THE TESTS FOR LIVERPOOL"
print t1
print t10
print query

c.execute("SELECT * FROM liverpool")
rows = c.fetchall()
for eachRow in rows:
    print eachRow
print "TEST FOR LIVERPOOL END"
#END OF TESTING--------------------------->>>

#<<<-------------------------------
#<<<-------------------------------LEICESTER------------------------------->>>
#------------------------------->>>


#LEICESTER TIME wunderground----------------------------------->>>
c.execute ("UPDATE leicester SET time= '%s' WHERE places='wundergrou'"%(time.time()))
#END LIVERPOOL TIME----------------------------------->>>

#LEICESTER TEMP wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/leicester.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_c']
lontemp = temp_f
print "Current temperature in %s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE leicester SET temp= '%s' WHERE places='wundergrou'"%(lontemp))

conn.commit()
#END LEICESTER TEMP----------------------------------->>>

#LEICESTER HUM wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/leicester.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['relative_humidity']
lonhum = temp_f
lonhum = lonhum.replace("%", "")
print "Current humidity in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE leicester SET hum= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END LEICESTER HUM----------------------------------->>>

#LEICESTER windspeed wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/leicester.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['wind_mph']
lonhum = temp_f
print "Current windspeed(mph) in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE leicester SET windspeed= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END LEICESTER windspeed----------------------------------->>>

#LEICESTER TIME open weather----------------------------------->>>
c.execute ("UPDATE leicester SET time= '%s' WHERE places='openweathe'"%(time.time()))
#END LEICESTER TIME----------------------------------->>>

#LEICESTER TEMP openweather----------------------------------->>>
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=leicester,uk&appid=4cb8ed260c2d5f12750c5a5107b9eb70')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['temp']
lontemp = temp_f
lontemp = lontemp - 273 #because kelvin to cel =- 273
print "Current temperature in open weather%s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE leicester SET temp= '%s' WHERE places='openweathe'"%(lontemp))

conn.commit()
#END LEICESTER TEMP----------------------------------->>>

#LEICESTER HUM openweather----------------------------------->>>
#got rid of the declaring f and other
parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['humidity']
lonhum = temp_f
print "Current humidity open weather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE leicester SET hum= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END LEICESTER HUM----------------------------------->>>

#LEICESTER windspeed open weather----------------------------------->>>
#got rid of the declaring f and other

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['wind']['speed']
lonhum = temp_f
# conversion metres per sec to mph
lonhum = lonhum * 3600 # secs to hours
lonhum = lonhum / 1609.344 #metres to miles

print "Current windspeed(mph) openweather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE leicester SET windspeed= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END LEICESTER windspeed----------------------------------->>>

#LEICESTER TIME darksky----------------------------------->>>
c.execute ("UPDATE leicester SET time= '%s' WHERE places='darksky'"%(time.time()))
#END LEICESTER TIME----------------------------------->>>

#LEICESTER TEMP darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.633333,-1.133333')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['temperature']
lontemp = temp_f
print "Current temperature darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp - 32 # convert to cel
lontemp = lontemp / 1.8
f.close()
print lontemp

c.execute ("UPDATE leicester SET temp= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LEICESTER TEMP----------------------------------->>>

#LEICESTER TIME darkspy----------------------------------->>>
c.execute ("UPDATE leicester SET time= '%s' WHERE places='darksky'"%(time.time()))
#END LEICESTER TIME----------------------------------->>>

#LEICESTER HUM darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.633333,-1.133333')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['humidity']
lontemp = temp_f
print "Current humidity darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp * 100
f.close()
print lontemp

c.execute ("UPDATE leicester SET hum= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LEICESTER TEMP----------------------------------->>>

#LEICESTER WINDSPEED darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.633333,-1.133333')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['windSpeed']
lontemp = temp_f
print "Current windspeed darksky in %s is: %s" % (location, temp_f)
f.close()
print lontemp

c.execute ("UPDATE leicester SET windspeed= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END LEICESTER TEMP----------------------------------->>>

#LEICESTER TIME averages----------------------------------->>>
c.execute ("UPDATE leicester SET time= '%s' WHERE places='final'"%(time.time()))
conn.commit()
#END LEICESTER TIME----------------------------------->>>

#LEICESTER TEMP averages----------------------------------->>>
c.execute("SELECT temp FROM leicester WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT temp FROM leicester WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT temp FROM leicester WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE leicester SET temp= '%s' WHERE places='final'"%(t10))
conn.commit()
#END LEICESTER TEMP----------------------------------->>>

#LEICESTER HUM averages----------------------------------->>>
c.execute("SELECT hum FROM leicester WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT hum FROM leicester WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT hum FROM leicester WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE leicester SET hum= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END LEICESTER HUM----------------------------------->>>

#LEICESTER WINSPEED averages----------------------------------->>>
c.execute("SELECT windspeed FROM leicester WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT windspeed FROM leicester WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT windspeed FROM leicester WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE leicester SET windspeed= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END LEICESTER WINDSPEED----------------------------------->>>

#TESTING LEICESTER----------------------------------->>>
print "THESE ARE THE TESTS FOR LEICESTER"
print t1
print t10
print query

c.execute("SELECT * FROM leicester")
rows = c.fetchall()
for eachRow in rows:
    print eachRow
print "TEST FOR LEICESTER END"
#END OF TESTING--------------------------->>>

#<<<-------------------------------
#<<<-------------------------------COVENTRY------------------------------->>>
#------------------------------->>>

#COVENTRY TIME wunderground----------------------------------->>>
c.execute ("UPDATE coventry SET time= '%s' WHERE places='wundergrou'"%(time.time()))
#END COVENTRY TIME----------------------------------->>>

#COVENTRY TEMP wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/coventry.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_c']
lontemp = temp_f
print "Current temperature in %s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE coventry SET temp= '%s' WHERE places='wundergrou'"%(lontemp))

conn.commit()
#END COVENTRY TEMP----------------------------------->>>

#COVENTRY HUM wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/coventry.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['relative_humidity']
lonhum = temp_f
lonhum = lonhum.replace("%", "")
print "Current humidity in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE coventry SET hum= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END COVENTRY HUM----------------------------------->>>

#COVENTRY windspeed wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/coventry.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['wind_mph']
lonhum = temp_f
print "Current windspeed(mph) in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE coventry SET windspeed= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END COVENTRY windspeed----------------------------------->>>

#COVENTRY TIME open weather----------------------------------->>>
c.execute ("UPDATE coventry SET time= '%s' WHERE places='openweathe'"%(time.time()))
#END COVENTRY TIME----------------------------------->>>

#COVENTRY TEMP openweather----------------------------------->>>
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=coventry,uk&appid=4cb8ed260c2d5f12750c5a5107b9eb70')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['temp']
lontemp = temp_f
lontemp = lontemp - 273 #because kelvin to cel =- 273
print "Current temperature in open weather%s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE coventry SET temp= '%s' WHERE places='openweathe'"%(lontemp))

conn.commit()
#END COVENTRY TEMP----------------------------------->>>

#COVENTRY HUM openweather----------------------------------->>>
#got rid of the declaring f and other
parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['humidity']
lonhum = temp_f
print "Current humidity open weather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE coventry SET hum= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END COVENTRY HUM----------------------------------->>>

#COVENTRY windspeed open weather----------------------------------->>>
#got rid of the declaring f and other

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['wind']['speed']
lonhum = temp_f
# conversion metres per sec to mph
lonhum = lonhum * 3600 # secs to hours
lonhum = lonhum / 1609.344 #metres to miles

print "Current windspeed(mph) openweather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE coventry SET windspeed= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END COVENTRY windspeed----------------------------------->>>

#COVENTRY TIME darksky----------------------------------->>>
c.execute ("UPDATE coventry SET time= '%s' WHERE places='darksky'"%(time.time()))
#END COVENTRY TIME----------------------------------->>>

#COVENTRY TEMP darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.405838,-1.512661')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['temperature']
lontemp = temp_f
print "Current temperature darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp - 32 # convert to cel
lontemp = lontemp / 1.8
f.close()
print lontemp

c.execute ("UPDATE coventry SET temp= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END COVENTRY TEMP----------------------------------->>>

#COVENTRY TIME darkspy----------------------------------->>>
c.execute ("UPDATE coventry SET time= '%s' WHERE places='darksky'"%(time.time()))
#END COVENTRY TIME----------------------------------->>>

#COVENTRY HUM darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.405838,-1.512661')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['humidity']
lontemp = temp_f
print "Current humidity darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp * 100
f.close()
print lontemp

c.execute ("UPDATE coventry SET hum= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END COVENTRY TEMP----------------------------------->>>

#COVENTRY WINDSPEED darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.405838,-1.512661')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['windSpeed']
lontemp = temp_f
print "Current windspeed darksky in %s is: %s" % (location, temp_f)
f.close()
print lontemp

c.execute ("UPDATE coventry SET windspeed= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END COVENTRY TEMP----------------------------------->>>

#COVENTRY TIME averages----------------------------------->>>
c.execute ("UPDATE coventry SET time= '%s' WHERE places='final'"%(time.time()))
conn.commit()
#END COVENTRY TIME----------------------------------->>>

#COVENTRY TEMP averages----------------------------------->>>
c.execute("SELECT temp FROM coventry WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT temp FROM coventry WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT temp FROM coventry WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE coventry SET temp= '%s' WHERE places='final'"%(t10))
conn.commit()
#END COVENTRY TEMP----------------------------------->>>

#COVENTRY HUM averages----------------------------------->>>
c.execute("SELECT hum FROM coventry WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT hum FROM coventry WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT hum FROM coventry WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE coventry SET hum= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END COVENTRY HUM----------------------------------->>>

#COVENTRY WINSPEED averages----------------------------------->>>
c.execute("SELECT windspeed FROM coventry WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT windspeed FROM coventry WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT windspeed FROM coventry WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE coventry SET windspeed= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END COVENTRY WINDSPEED----------------------------------->>>

#TESTING COVENTRY----------------------------------->>>
print "THESE ARE THE TESTS FOR COVENTRY"
print t1
print t10
print query

c.execute("SELECT * FROM coventry")
rows = c.fetchall()
for eachRow in rows:
    print eachRow
print "TEST FOR COVENTRY END"
#END OF TESTING--------------------------->>>

#<<<-------------------------------
#<<<-------------------------------BRISTOL------------------------------->>>
#------------------------------->>>


#BRISTOL TIME wunderground----------------------------------->>>
c.execute ("UPDATE bristol SET time= '%s' WHERE places='wundergrou'"%(time.time()))
#END BRISTOL TIME----------------------------------->>>

#BRISTOL TEMP wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/bristol.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_c']
lontemp = temp_f
print "Current temperature in %s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE bristol SET temp= '%s' WHERE places='wundergrou'"%(lontemp))

conn.commit()
#END BRISTOL TEMP----------------------------------->>>

#BRISTOL HUM wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/bristol.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['relative_humidity']
lonhum = temp_f
lonhum = lonhum.replace("%", "")
print "Current humidity in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE bristol SET hum= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END BRISTOL HUM----------------------------------->>>

#BRISTOL windspeed wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/bristol.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['wind_mph']
lonhum = temp_f
print "Current windspeed(mph) in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE bristol SET windspeed= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END BRISTOL windspeed----------------------------------->>>

#BRISTOL TIME open weather----------------------------------->>>
c.execute ("UPDATE bristol SET time= '%s' WHERE places='openweathe'"%(time.time()))
#END BRISTOL TIME----------------------------------->>>

#BRISTOL TEMP openweather----------------------------------->>>
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=bristol,uk&appid=4cb8ed260c2d5f12750c5a5107b9eb70')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['temp']
lontemp = temp_f
lontemp = lontemp - 273 #because kelvin to cel =- 273
print "Current temperature in open weather%s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE bristol SET temp= '%s' WHERE places='openweathe'"%(lontemp))

conn.commit()
#END BRISTOL TEMP----------------------------------->>>

#BRISTOL HUM openweather----------------------------------->>>
#got rid of the declaring f and other
parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['humidity']
lonhum = temp_f
print "Current humidity open weather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE bristol SET hum= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END BRISTOL HUM----------------------------------->>>

#BRISTOL windspeed open weather----------------------------------->>>
#got rid of the declaring f and other

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['wind']['speed']
lonhum = temp_f
# conversion metres per sec to mph
lonhum = lonhum * 3600 # secs to hours
lonhum = lonhum / 1609.344 #metres to miles

print "Current windspeed(mph) openweather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE bristol SET windspeed= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END BRISTOL windspeed----------------------------------->>>

#BRISTOL TIME darksky----------------------------------->>>
c.execute ("UPDATE bristol SET time= '%s' WHERE places='darksky'"%(time.time()))
#END BRISTOL TIME----------------------------------->>>

#BRISTOL TEMP darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/51.455313,-2.591902')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['temperature']
lontemp = temp_f
print "Current temperature darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp - 32 # convert to cel
lontemp = lontemp / 1.8
f.close()
print lontemp

c.execute ("UPDATE bristol SET temp= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END BRISTOL TEMP----------------------------------->>>

#BRISTOL TIME darkspy----------------------------------->>>
c.execute ("UPDATE bristol SET time= '%s' WHERE places='darksky'"%(time.time()))
#END BRISTOL TIME----------------------------------->>>

#BRISTOL HUM darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/51.455313,-2.591902')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['humidity']
lontemp = temp_f
print "Current humidity darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp * 100
f.close()
print lontemp

c.execute ("UPDATE bristol SET hum= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END BRISTOL TEMP----------------------------------->>>

#BRISTOL WINDSPEED darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/51.455313,-2.591902')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['windSpeed']
lontemp = temp_f
print "Current windspeed darksky in %s is: %s" % (location, temp_f)
f.close()
print lontemp

c.execute ("UPDATE bristol SET windspeed= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END BRISTOL TEMP----------------------------------->>>

#BRISTOL TIME averages----------------------------------->>>
c.execute ("UPDATE bristol SET time= '%s' WHERE places='final'"%(time.time()))
conn.commit()
#END BRISTOL TIME----------------------------------->>>

#BRISTOL TEMP averages----------------------------------->>>
c.execute("SELECT temp FROM bristol WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT temp FROM bristol WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT temp FROM bristol WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE bristol SET temp= '%s' WHERE places='final'"%(t10))
conn.commit()
#END BRISTOL TEMP----------------------------------->>>

#BRISTOL HUM averages----------------------------------->>>
c.execute("SELECT hum FROM bristol WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT hum FROM bristol WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT hum FROM bristol WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE bristol SET hum= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END BRISTOL HUM----------------------------------->>>

#BRISTOL WINSPEED averages----------------------------------->>>
c.execute("SELECT windspeed FROM bristol WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT windspeed FROM bristol WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT windspeed FROM bristol WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE bristol SET windspeed= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END BRISTOL WINDSPEED----------------------------------->>>

#TESTING BRISTOL----------------------------------->>>
print "THESE ARE THE TESTS FOR BRISTOL"
print t1
print t10
print query

c.execute("SELECT * FROM bristol")
rows = c.fetchall()
for eachRow in rows:
    print eachRow
print "TEST FOR BRISTOL END"
#END OF TESTING--------------------------->>>

#<<<-------------------------------
#<<<-------------------------------BIRMINGHAM------------------------------->>>
#------------------------------->>>


#BIRMINGHAM TIME wunderground----------------------------------->>>
c.execute ("UPDATE birmingham SET time= '%s' WHERE places='wundergrou'"%(time.time()))
#END BIRMINGHAM TIME----------------------------------->>>

#BIRMINGHAM TEMP wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/birmingham.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_c']
lontemp = temp_f
print "Current temperature in %s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE birmingham SET temp= '%s' WHERE places='wundergrou'"%(lontemp))

conn.commit()
#END BIRMINGHAM TEMP----------------------------------->>>

#BIRMINGHAM HUM wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/birmingham.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['relative_humidity']
lonhum = temp_f
lonhum = lonhum.replace("%", "")
print "Current humidity in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE birmingham SET hum= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END BIRMINGHAM HUM----------------------------------->>>

#BIRMINGHAM windspeed wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/birmingham.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['wind_mph']
lonhum = temp_f
print "Current windspeed(mph) in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE birmingham SET windspeed= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END BIRMINGHAM windspeed----------------------------------->>>

#BIRMINGHAM TIME open weather----------------------------------->>>
c.execute ("UPDATE birmingham SET time= '%s' WHERE places='openweathe'"%(time.time()))
#END BIRMINGHAM TIME----------------------------------->>>

#BIRMINGHAM TEMP openweather----------------------------------->>>
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=birmingham,uk&appid=4cb8ed260c2d5f12750c5a5107b9eb70')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['temp']
lontemp = temp_f
lontemp = lontemp - 273 #because kelvin to cel =- 273
print "Current temperature in open weather%s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE birmingham SET temp= '%s' WHERE places='openweathe'"%(lontemp))

conn.commit()
#END BIRMINGHAM TEMP----------------------------------->>>

#BIRMINGHAM HUM openweather----------------------------------->>>
#got rid of the declaring f and other
parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['humidity']
lonhum = temp_f
print "Current humidity open weather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE birmingham SET hum= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END BIRMINGHAM HUM----------------------------------->>>

#BIRMINGHAM windspeed open weather----------------------------------->>>
#got rid of the declaring f and other

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['wind']['speed']
lonhum = temp_f
# conversion metres per sec to mph
lonhum = lonhum * 3600 # secs to hours
lonhum = lonhum / 1609.344 #metres to miles

print "Current windspeed(mph) openweather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE birmingham SET windspeed= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END BIRMINGHAM windspeed----------------------------------->>>

#BIRMINGHAM TIME darksky----------------------------------->>>
c.execute ("UPDATE birmingham SET time= '%s' WHERE places='darksky'"%(time.time()))
#END BIRMINGHAM TIME----------------------------------->>>

#BIRMINGHAM TEMP darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.482961,-1.893592')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['temperature']
lontemp = temp_f
print "Current temperature darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp - 32 # convert to cel
lontemp = lontemp / 1.8
f.close()
print lontemp

c.execute ("UPDATE birmingham SET temp= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END BIRMINGHAM TEMP----------------------------------->>>

#BIRMINGHAM TIME darkspy----------------------------------->>>
c.execute ("UPDATE birmingham SET time= '%s' WHERE places='darksky'"%(time.time()))
#END BIRMINGHAM TIME----------------------------------->>>

#BIRMINGHAM HUM darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.482961,-1.893592')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['humidity']
lontemp = temp_f
print "Current humidity darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp * 100
f.close()
print lontemp

c.execute ("UPDATE birmingham SET hum= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END BIRMINGHAM TEMP----------------------------------->>>

#BIRMINGHAM WINDSPEED darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.482961,-1.893592')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['windSpeed']
lontemp = temp_f
print "Current windspeed darksky in %s is: %s" % (location, temp_f)
f.close()
print lontemp

c.execute ("UPDATE birmingham SET windspeed= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END BIRMINGHAM TEMP----------------------------------->>>

#BIRMINGHAM TIME averages----------------------------------->>>
c.execute ("UPDATE birmingham SET time= '%s' WHERE places='final'"%(time.time()))
conn.commit()
#END BIRMINGHAM TIME----------------------------------->>>

#BIRMINGHAM TEMP averages----------------------------------->>>
c.execute("SELECT temp FROM birmingham WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT temp FROM birmingham WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT temp FROM birmingham WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE birmingham SET temp= '%s' WHERE places='final'"%(t10))
conn.commit()
#END BIRMINGHAM TEMP----------------------------------->>>

#BIRMINGHAM HUM averages----------------------------------->>>
c.execute("SELECT hum FROM birmingham WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT hum FROM birmingham WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT hum FROM birmingham WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE birmingham SET hum= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END BIRMINGHAM HUM----------------------------------->>>

#BIRMINGHAM WINSPEED averages----------------------------------->>>
c.execute("SELECT windspeed FROM birmingham WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT windspeed FROM birmingham WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT windspeed FROM birmingham WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE birmingham SET windspeed= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END BIRMINGHAM WINDSPEED----------------------------------->>>

#TESTING BIRMINGHAM----------------------------------->>>
print "THESE ARE THE TESTS FOR BIRMINGHAM"
print t1
print t10
print query

c.execute("SELECT * FROM birmingham")
rows = c.fetchall()
for eachRow in rows:
    print eachRow
print "TEST FOR BIRMINGHAM END"
#END OF TESTING--------------------------->>>

#<<<-------------------------------
#<<<-------------------------------NOTTINGHAM------------------------------->>>
#------------------------------->>>


#NOTTINGHAM TIME wunderground----------------------------------->>>
c.execute ("UPDATE nottingham SET time= '%s' WHERE places='wundergrou'"%(time.time()))
#END NOTTINGHAM TIME----------------------------------->>>

#NOTTINGHAM TEMP wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/nottingham.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_c']
lontemp = temp_f
print "Current temperature in %s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE nottingham SET temp= '%s' WHERE places='wundergrou'"%(lontemp))

conn.commit()
#END NOTTINGHAM TEMP----------------------------------->>>

#NOTTINGHAM HUM wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/nottingham.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['relative_humidity']
lonhum = temp_f
lonhum = lonhum.replace("%", "")
print "Current humidity in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE nottingham SET hum= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END NOTTINGHAM HUM----------------------------------->>>

#NOTTINGHAM windspeed wunderground----------------------------------->>>
f = urllib2.urlopen('http://api.wunderground.com/api/c2d6a825ad8f369b/geolookup/conditions/q/gb/nottingham.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['wind_mph']
lonhum = temp_f
print "Current windspeed(mph) in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE nottingham SET windspeed= '%s' WHERE places='wundergrou'"%(lonhum))

conn.commit()
#END NOTTINGHAM windspeed----------------------------------->>>

#NOTTINGHAM TIME open weather----------------------------------->>>
c.execute ("UPDATE nottingham SET time= '%s' WHERE places='openweathe'"%(time.time()))
#END NOTTINGHAM TIME----------------------------------->>>

#NOTTINGHAM TEMP openweather----------------------------------->>>
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=nottingham,uk&appid=4cb8ed260c2d5f12750c5a5107b9eb70')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['temp']
lontemp = temp_f
lontemp = lontemp - 273 #because kelvin to cel =- 273
print "Current temperature in open weather%s is: %s" % (location, temp_f)

f.close()
print lontemp

c.execute ("UPDATE nottingham SET temp= '%s' WHERE places='openweathe'"%(lontemp))

conn.commit()
#END NOTTINGHAM TEMP----------------------------------->>>

#NOTTINGHAM HUM openweather----------------------------------->>>
#got rid of the declaring f and other
parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['main']['humidity']
lonhum = temp_f
print "Current humidity open weather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE nottingham SET hum= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END NOTTINGHAM HUM----------------------------------->>>

#NOTTINGHAM windspeed open weather----------------------------------->>>
#got rid of the declaring f and other

parsed_json = json.loads(json_string)

location = parsed_json['name']

temp_f = parsed_json['wind']['speed']
lonhum = temp_f
# conversion metres per sec to mph
lonhum = lonhum * 3600 # secs to hours
lonhum = lonhum / 1609.344 #metres to miles

print "Current windspeed(mph) openweather in %s is: %s" % (location, temp_f)

f.close()
print lonhum

c.execute ("UPDATE nottingham SET windspeed= '%s' WHERE places='openweathe'"%(lonhum))

conn.commit()
#END NOTTINGHAM windspeed----------------------------------->>>

#NOTTINGHAM TIME darksky----------------------------------->>>
c.execute ("UPDATE nottingham SET time= '%s' WHERE places='darksky'"%(time.time()))
#END NOTTINGHAM TIME----------------------------------->>>

#NOTTINGHAM TEMP darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.954783,-1.158109')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['temperature']
lontemp = temp_f
print "Current temperature darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp - 32 # convert to cel
lontemp = lontemp / 1.8
f.close()
print lontemp

c.execute ("UPDATE nottingham SET temp= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END NOTTINGHAM TEMP----------------------------------->>>

#NOTTINGHAM TIME darkspy----------------------------------->>>
c.execute ("UPDATE nottingham SET time= '%s' WHERE places='darksky'"%(time.time()))
#END NOTTINGHAM TIME----------------------------------->>>

#NOTTINGHAM HUM darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.954783,-1.158109')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['humidity']
lontemp = temp_f
print "Current humidity darksky in %s is: %s" % (location, temp_f)
lontemp = lontemp * 100
f.close()
print lontemp

c.execute ("UPDATE nottingham SET hum= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END NOTTINGHAM TEMP----------------------------------->>>

#NOTTINGHAM WINDSPEED darksky----------------------------------->>>
f = urllib2.urlopen('https://api.forecast.io/forecast/5eede7dcce890cd8e0324453966f8672/52.954783,-1.158109')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['timezone']

temp_f = parsed_json['currently']['windSpeed']
lontemp = temp_f
print "Current windspeed darksky in %s is: %s" % (location, temp_f)
f.close()
print lontemp

c.execute ("UPDATE nottingham SET windspeed= '%s' WHERE places='darksky'"%(lontemp))

conn.commit()
#END NOTTINGHAM TEMP----------------------------------->>>

#NOTTINGHAM TIME averages----------------------------------->>>
c.execute ("UPDATE nottingham SET time= '%s' WHERE places='final'"%(time.time()))
conn.commit()
#END NOTTINGHAM TIME----------------------------------->>>

#NOTTINGHAM TEMP averages----------------------------------->>>
c.execute("SELECT temp FROM nottingham WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT temp FROM nottingham WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT temp FROM nottingham WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE nottingham SET temp= '%s' WHERE places='final'"%(t10))
conn.commit()
#END NOTTINGHAM TEMP----------------------------------->>>

#NOTTINGHAM HUM averages----------------------------------->>>
c.execute("SELECT hum FROM nottingham WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT hum FROM nottingham WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT hum FROM nottingham WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE nottingham SET hum= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END NOTTINGHAM HUM----------------------------------->>>

#NOTTINGHAM WINSPEED averages----------------------------------->>>
c.execute("SELECT windspeed FROM nottingham WHERE places='darksky'")
t1 = c.fetchone()
t1 = t1[0]
c.execute("SELECT windspeed FROM nottingham WHERE places='openweathe'")
t2 = c.fetchone()
t2 = t2[0]
c.execute("SELECT windspeed FROM nottingham WHERE places='wundergrou'")
t3 = c.fetchone()
t3 = t3[0]
t10 = t1 + t2 + t3
t10 = t10 / 3
c.execute ("UPDATE nottingham SET windspeed= '%s' WHERE places='final'"%(t10))
conn.commit()
#
#END NOTTINGHAM WINDSPEED----------------------------------->>>

#TESTING NOTTINGHAM----------------------------------->>>
print "THESE ARE THE TESTS FOR NOTTINGHAM"
print t1
print t10
print query

c.execute("SELECT * FROM nottingham")
rows = c.fetchall()
for eachRow in rows:
    print eachRow
print "TEST FOR NOTTINGHAM END"
#END OF TESTING--------------------------->>>


#<<<-------------------------------
#<<<-------------------------------AVERAGES------------------------------->>>
#------------------------------->>>

#<<<-------------------------------AVERAGE TEMP------------------------------->>>
c.execute ("UPDATE averages SET time= '%s' WHERE name='averagetemp'"%(time.time()))

c.execute("SELECT temp FROM london WHERE places='final'")
lontemp = c.fetchone()
lontemp = lontemp[0]

c.execute("SELECT temp FROM birmingham WHERE places='final'")
birtemp = c.fetchone()
birtemp = birtemp[0]

c.execute("SELECT temp FROM bristol WHERE places='final'")
britemp = c.fetchone()
britemp = britemp[0]

c.execute("SELECT temp FROM coventry WHERE places='final'")
covtemp = c.fetchone()
covtemp = covtemp[0]

c.execute("SELECT temp FROM leicester WHERE places='final'")
leitemp = c.fetchone()
leitemp = leitemp[0]

c.execute("SELECT temp FROM liverpool WHERE places='final'")
livtemp = c.fetchone()
livtemp = livtemp[0]

c.execute("SELECT temp FROM manchester WHERE places='final'")
mantemp = c.fetchone()
mantemp = mantemp[0]

c.execute("SELECT temp FROM nottingham WHERE places='final'")
nottemp = c.fetchone()
nottemp = nottemp[0]

avtemp = lontemp + birtemp + britemp + covtemp + leitemp + livtemp + mantemp + nottemp
avtemp = avtemp / 8
print "this is avtemp"
print avtemp

c.execute ("UPDATE averages SET value= '%s' WHERE name='averagetemp'"%(avtemp))
conn.commit()
#END AVERAGE TEMP----------------------------------->>>

#<<<-------------------------------AVERAGE HUM------------------------------->>>
c.execute ("UPDATE averages SET time= '%s' WHERE name='averagehum'"%(time.time()))

c.execute("SELECT hum FROM london WHERE places='final'")
lonhum = c.fetchone()
lonhum = lonhum[0]

c.execute("SELECT hum FROM birmingham WHERE places='final'")
birhum = c.fetchone()
birhum = birhum[0]

c.execute("SELECT hum FROM bristol WHERE places='final'")
brihum = c.fetchone()
brihum = brihum[0]

c.execute("SELECT hum FROM coventry WHERE places='final'")
covhum = c.fetchone()
covhum = covhum[0]

c.execute("SELECT hum FROM leicester WHERE places='final'")
leihum = c.fetchone()
leihum = leihum[0]

c.execute("SELECT hum FROM liverpool WHERE places='final'")
livhum = c.fetchone()
livhum = livhum[0]

c.execute("SELECT hum FROM manchester WHERE places='final'")
manhum = c.fetchone()
manhum = manhum[0]

c.execute("SELECT hum FROM nottingham WHERE places='final'")
nothum = c.fetchone()
nothum = nothum[0]

avhum = lonhum + birhum + brihum + covhum + leihum + livhum + manhum + nothum
avhum = avhum / 8
print "this is avhum"
print avhum

c.execute ("UPDATE averages SET value= '%s' WHERE name='averagehum'"%(avhum))
conn.commit()

#END AVERAGE HUM----------------------------------->>>

#<<<-------------------------------AVERAGE WIND------------------------------->>>
c.execute ("UPDATE averages SET time= '%s' WHERE name='averagewind'"%(time.time()))

c.execute("SELECT windspeed FROM london WHERE places='final'")
lonwind = c.fetchone()
lonwind = lonwind[0]

c.execute("SELECT windspeed FROM birmingham WHERE places='final'")
birwind = c.fetchone()
birwind = birwind[0]

c.execute("SELECT windspeed FROM bristol WHERE places='final'")
briwind = c.fetchone()
briwind = briwind[0]

c.execute("SELECT windspeed FROM coventry WHERE places='final'")
covwind = c.fetchone()
covwind = covwind[0]

c.execute("SELECT windspeed FROM leicester WHERE places='final'")
leiwind = c.fetchone()
leiwind = leiwind[0]

c.execute("SELECT windspeed FROM liverpool WHERE places='final'")
livwind = c.fetchone()
livwind = livwind[0]

c.execute("SELECT windspeed FROM manchester WHERE places='final'")
manwind = c.fetchone()
manwind = manwind[0]

c.execute("SELECT windspeed FROM nottingham WHERE places='final'")
notwind = c.fetchone()
notwind = notwind[0]

avwind = lonwind + birwind + briwind + covwind + leiwind + livwind + manwind + notwind
avwind = avwind / 8
print "this is avwind"
print avwind

c.execute ("UPDATE averages SET value= '%s' WHERE name='averagewind'"%(avwind))
conn.commit()


#END AVERAGE WIND----------------------------------->>>

