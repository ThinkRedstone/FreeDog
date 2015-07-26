#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 26, 2015 12:43:27 PM$"

import MySQLdb
def startConnection(database):
    global db
    db = MySQLdb.connect("localhost","root", "raspberry",database)

def execute(sql):
    global db
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "Cannot execute: ", sql
        db.rollback()

def executeSelect(sql):
    global db
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        print "Cannot execute select: ", sql

if __name__ == "__main__":
    startConnection("horse")
    execute("insert into bla values(5, 'blu')")
    rows = executeSelect("select * from bla;")
    for row in rows:
        print "num: ", row[0] , "name: ", row[1]
