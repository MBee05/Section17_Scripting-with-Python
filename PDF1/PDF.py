import PyPDF2

with open('dummy.pdf', 'rb') as file:
    # print(file)
# output    <_io.TextIOWrapper name='dummy.pdf' mode='r' encoding='cp1252'>
    reader=PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
# output    1 which is 1pg

    # print(reader.getPage(0))
# output    display object
# {'/Type': '/Page', '/Parent': IndirectObject(4, 0), '/Resources': IndirectObject(11, 0), '/MediaBox': [0, 0, 595, 842], '/Group': {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I': <PyPDF2.generic.BooleanObject object at 0x00000222EC8B67D0>}, '/Contents': IndirectObject(2, 0)}

    # print(reader.rotate(180))
    
# error so 
    page=reader.getPage(0)
    # print(page.rotateCounterClockwise(90))
    
# display   object in the memory
# {'/Type': '/Page', '/Parent': IndirectObject(4, 0), '/Resources': IndirectObject(11, 0), '/MediaBox': [0, 0, 595, 842], '/Group': {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I': <PyPDF2.generic.BooleanObject object at 0x00000207B03C66D0>}, '/Contents': IndirectObject(2, 0), '/Rotate': -180}

    # rotated the pg and with writer obj we can add writer.addPage(page)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)    

# it creates a new_file named 'tilt.pdf'
# it opens rotated while opening it 