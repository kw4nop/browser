#!/usr/bin/env python

from twill.commands import *
import twill

class Browser:

    def __init__ (self, ua="robotina-ua", timeout=200):

        self.commands = twill.commands
        self.commands.agent = ua
        self.commands.timeout = timeout


    def source_code (self, url=None):

        if url:
            try:
                self.commands.go(url)
            except:
                print "There is a problem with the URL"
            sc = self.commands.get_browser().get_html()
        else:
            sc = "Please provide the URL"

        return sc


def main():
    print "."

if __name__ == "__main__":
    exit (main())
