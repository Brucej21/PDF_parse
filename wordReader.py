#word reader
# Import the module
from docx import Document
from docx.shared import Pt
import csv

'''
data  = csv.reader(open("wordPatterns.csv"), delimiter=",")
fields = data.next()

for row in data:
	print data
'''
#https://newcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files
f = open('wordPatterns.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print row[1]




# Open the .docx file
#document = opendocx('docExmaple.docx')

doc= Document('test2.docx')


for p in doc.paragraphs:
        if 'this researcher identified' in p.text:
            print('SEARCH FOUND!!')
            text = p.text.replace('this researcher identified ', 'new text')
            style = p.style
            p.text = text
            p.style = style
    # doc.save(filename)
doc.save('test3.docx')