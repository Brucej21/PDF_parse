#PDF extraction work
import PyPDF2
pdfFileObj = open('TargetPDF.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#pdfReader.numPages
pageObj = pdfReader.getPage(1)
pageObj.extractText()
