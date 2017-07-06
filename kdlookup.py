#!/usr/bin/env python
''' Demarche:
1. Get file name and type
2. File object - vet the file
3. First pass - Raw data - extract relevant lines of data - put in list
    possible types = CSV , sysinfo, DriverTrace, 
4. Do the actual analysis 
    - DriverTrace packet timing
    - Device history -
    - Server restarts 
import re

textfile = open(filename, 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("(<(\d{4,5})>)?", filetext)
'''
import re 
def lookupios(iosname):
    try:
        fh=open(iosname,  'r', errors='ignore')
        print('fh = ', str(fh))
        kdtext=fh.read()
        fh.close 
#        rgx = re.compile(r'^\s+-+Unit Statistics.\nUnit:\s+(?P<UnitName>\w+)(?:[^:]+\:\s+)(?P<IOServer>\w+)\s.*?Name:\s+(?P<PortName>\w+)\s')
#        rgxp = r'^\s+-+Unit Statistics.\nUnit:\s+(?P<UnitName>\w+)(?:[^:]+\:\s+)(?P<IOServer>\w+)\s.*?Name:\s+(?P<PortName>\w+)\s'
        rgxp = r"^\s+-+Unit Statistics.\nUnit:\s+(?P<UnitName>\w+)"
        matches = re.findall(rgxp, kdtext)
        print('found this many matches ')
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno,strerror))
        print('kann Datei nicht öffnen:', str(fh))
def main():
    iosname="logs/kdump1.dat"
    lookupios(iosname)
main() 
    
