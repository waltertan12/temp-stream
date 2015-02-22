import time
import datetime
import sqlite3 as lite
import sys

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-0000065d9c99/w1_slave")
	text = tempfile.read().split("\n")[1].split(" ")[9]
	tempfile.close()
	temp = float(text[2:])/1000
	return temp

def toF(temp):
	return temp * (9.0/5.0) + 32.0

def logData(temp):
	conn = lite.connect('temp.db')
	cur = conn.cursor()
	try:		
		cur.execute("INSERT INTO tbl VALUES (? , ?)",[toF(readTemp()),datetime.datetime.now()])
		conn.commit()
	except lite.Error, e:
		if conn:
			conn.rollback()
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if conn:
			conn.close()
