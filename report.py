from fpdf import FPDF
import os

img_path = 'img/miro.jpg'
file_name = "test.pdf"
header_size = 24

def setFooter():
    pdf.set_y(250)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0,10, 'Page %s' % pdf.page_no(), 0, 0, 'C')

if __name__=="__main__":
    pdf = FPDF()

    # PAGE 1
    pdf.add_page()
    

    # HEADER
    pdf.set_font('Arial', 'B', header_size)
    pdf.cell(20, 10, 'Antenna TEST')

    # LOGO
    pdf.image(img_path, x = 130, y = -10, w = 70, h = 70, type = 'JPG', link = '')

    # PAGE NUMBER
    setFooter()

    # PAGE 2
    pdf.add_page()

    # HEADER
    pdf.set_font('Arial', 'B', header_size)
    pdf.cell(20, 10, 'Title', 1, 1, 'C')

    # LOGO
    pdf.image(img_path, x = 130, y = -10, w = 70, h = 70, type = 'JPG', link = '')

    # PAGE NUMBER
    setFooter()


    # GENERATE FILE
    if os.path.exists(file_name):
        os.remove(file_name)
    
    pdf.output(file_name, 'F')