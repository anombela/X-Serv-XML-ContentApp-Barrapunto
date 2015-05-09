#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys


class myContentHandler (ContentHandler):

    def __init__(self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.link = ""
        self.name = ""
        self.salida = ""

    def startElement(self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement(self, name):
        if name == 'item':
            self.salida += ("-Title:  <a href=" + self.link + ">" +
                            self.name + "</a>\n<br>")
            self.name = ""
            self.link = ""
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.name = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                self.link = self.theContent
                self.inContent = False
                self.theContent = ""

    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

def getNews():

    # Load parser and driver

    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)

    # Ready, set, go!
    theParser.parse("http://barrapunto.com/index.rss")
    return  theHandler.salida
