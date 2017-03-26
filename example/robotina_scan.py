#!/usr/bin/env python

from browser import Browser
import sys,re

def main():

    folders = []
    
    try:
        URL = sys.argv[1] + "/scanner.php?srun&"+ sys.argv[2] +"&scandirs="
        print URL
    except:
        print 'Usage: robotina.py -i <url> <version>'
        sys.exit(2)

    browser = Browser("Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",600)

    #list of folders in the / directory
    source = browser.source_code(URL)
    for list in re.finditer (r'''(\.\/)(.*)''', source):
        folders.append(list.group(2))

    #print "\n".join([str(f) for f in folders])
    

    for folder in folders:
         #Source code
         source = browser.source_code(URL+folder)
         
         #CLEAN
         for clean in re.finditer (r'''(CLEARED).*(: ).*(Cleared malware from file:.*) (Details:.*)''', source):
             print ''.join(str(s) for s in clean.groups())

         #WARNS
         for warns in re.finditer (r'''(WARN).*(: Found.*: )<.*">(.*)<\/.*(\(NOT CLEANED.*\)):''', source):
             print ''.join(str(s) for s in warns.groups())


         #ERRORS
         for errors in re.finditer (r'''(ERROR).*''', source):
             print "\n"+errors.group(0) 

         #links = showlinks()
         #for link in links:
         #    print link.base_url 
         
if __name__ == "__main__":
    exit (main())
