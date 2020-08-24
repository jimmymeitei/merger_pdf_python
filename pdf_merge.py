# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:19:37 2020

@author: OKJS
"""
from PyPDF2 import PdfFileMerger, PdfFileReader
 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()
 
# I had 5 files in the folder that had to be merged into a single document
# Loop through all of them and append their pages
for fileNumber in range(1, 5):
    mergedObject.append(PdfFileReader('pro_' + str(fileNumber)+ '.pdf', 'rb'))
 
# Write all the files into a file which is named as shown below
mergedObject.write("mergedfilesoutput.pdf")