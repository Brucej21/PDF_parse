#word reader
# Import the module
from docx import Document
from docx.shared import Pt
# Open the .docx file
#document = opendocx('docExmaple.docx')

doc= Document('test2.docx')

'''
sections = document.sections
for section in sections:
    print(section.start_type)
    document.save('Test.docx')
'''
'''
style = doc.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(10)
'''



'''
for paragraph in document.paragraphs:
    if 'this researcher identified ' in paragraph.text:
        print paragraph.text
        paragraph.text = 'new text containing ocean'
        document.save('Test.docx')
 '''
for p in doc.paragraphs:
        if 'this researcher identified' in p.text:
            print('SEARCH FOUND!!')
            text = p.text.replace('this researcher identified ', 'new text')
            style = p.style
            p.text = text
            p.style = style
    # doc.save(filename)
doc.save('test3.docx')
            
#return 1
