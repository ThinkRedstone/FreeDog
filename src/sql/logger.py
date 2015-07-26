#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thinkredstone"
__date__ = "$Jul 26, 2015 1:27:44 PM$"
from sqlProcessing import *
from threading import Thread
from time import sleep

class Logger(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        startConnection("horse")
        self.index = 0
    def run(self):
        while self.running:
            log(self.index, 1, 2)
            self.index += 1
            sleep(1)
            
def log(index, long, lat):
    execute("insert into bla values(%d,%d,%d)" % (index, long, lat))
    
def startLogger():
    global logger
    logger = Logger()
    logger.start()
    
def stopLogger():
    global logger
    logger.running = False
    logger.join()

if __name__ == "__main__":
    startLogger()
    sleep(15)
    stopLogger()
