#!/usr/bin/env python

import twill.commands
from twill.utils import print_form
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


    def show_forms (self, url, filename="forms"):
        
        if url:
            try:
                self.commands.go(url)
            except:
                print "There is a problem with the URL"
            forms  = self.commands.get_browser().get_all_forms()
            stream = open(filename, 'w')

            for i, form in enumerate(forms):
                     print_form (i,form,stream)            
        else:
            sc = "Please provide the URL"
            

    def simple_login (self, url = None):

        if url:
            try:
                self.commands.go(url)
            except:
                print "There is a problem with the URL"

            #testing
            self.commands.formclear('2')
            self.commands.fv("2", "session_key", "")
            self.commands.fv("2", "session_password", "")
            self.commands.submit()
          
        else:
             response = "Please provide the URL"

        #return self.commands.get_browser()
        #return self.commands.get_browser().get_url()
        #return self.commands.get_browser().get_html()
        #return self.commands.get_browser().get_title()
        

        

    


def main():
    print "."

if __name__ == "__main__":
    exit (main())
