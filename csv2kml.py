# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:46:37 2016
#http://stackoverflow.com/questions/7529538/create-kml-from-csv-in-python
@author: Lieven and Jason
"""

from osgeo import ogr
import os
import csv
os.chdir('/home/user/Desktop/geoscripting/lesson14')



for row in input_file:
    print row
    
import csv
#Input the file name.
fname = "results.csv"
data = csv.reader(open(fname), delimiter = ',')
#Skip the 1st header row.
data.next()
#Open the file to be written.
f = open('csv2kml.kml', 'w')

#Writing the kml file.
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
f.write("<Document>\n")
f.write("   <name>" + fname + '.kml' +"</name>\n")
for row in data:
    f.write("   <Placemark>\n")
    f.write("       <name>" + str(row[0]) + "</name>\n")
    f.write("       <description>" + str(row[1]) + "</description>\n")
    f.write("       <Point>\n")
    f.write("           <coordinates>" + str(row[2]) + "," + str(row[3]) + "," + str(row[2]) + "</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")
f.write("</Document>\n")
f.write("</kml>\n")
f.close()
print "File Created. "
