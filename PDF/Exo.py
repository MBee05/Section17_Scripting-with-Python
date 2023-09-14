import PyPDF2
import sys
# combined the 3 pdf
# pdf.py dummy.pdf twopage.pdf tilt.pdf

# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     for pdf in pdf_list:
#         print(pdf)

# pdf_combiner(inputs)

# PS C:\Users\Mohamed Bee\Desktop\Python_w_Udemy\Section17_Scripting with Python\PDF> python Exo.py dummy.pdf twopage.pdf tilt.pdf
# output
# dummy.pdf
# twopage.pdf
# tilt.pdf


# that is bcz there is the merger obj.

# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger=PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
    
# pdf_combiner(inputs)

# type all that then enter
# PS C:\Users\Mohamed Bee\Desktop\Python_w_Udemy\Section17_Scripting with Python\PDF> python Exo.py dummy.pdf twopage.pdf tilt.pdf

# output
# dummy.pdf
# twopage.pdf
# tilt.pdf
# and then run the program


template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output= PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page= template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
        
        
        
# output pages are watermarked
        