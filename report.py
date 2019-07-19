from fpdf import FPDF
import os

img_path = 'img/miro.jpg'
plot_vertical_path = 'img/antenna_1.png'
plot_horizontal_path = 'img/antenna_1.png'
file_name = "test.pdf"
header_size = 24
plot_y = 80
plot_x = 40
plot_size = 130

class PDF(FPDF):
    def header(self):
        # Logo
        self.image(img_path, x = 130, y = -10, w = 70, h = 70, type = 'JPG', link = '')

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


if __name__=="__main__":
    pdf = PDF()
    pdf.alias_nb_pages()

    # PAGE 1
    pdf.add_page()
    
    # HEADER
    pdf.set_font('Arial', 'B', header_size)
    pdf.ln(40)
    pdf.cell(20, 10, 'Antenna VERTICAL')

    # PLOT VERTICAL
    pdf.image(plot_vertical_path, x = plot_x, y = plot_y, w = plot_size, h = plot_size, type = 'PNG', link = '')

    # # PAGE 2
    pdf.add_page()

    # # HEADER
    pdf.set_font('Arial', 'B', header_size)
    pdf.ln(40)
    pdf.cell(20, 10, 'Antenna HORIZONTAL')

    # PLOT HORIZONTAL
    pdf.image(plot_horizontal_path, x = plot_x, y = plot_y, w = plot_size, h = plot_size, type = 'PNG', link = '')

    # GENERATE FILE
    if os.path.exists(file_name):
        os.remove(file_name)
    
    pdf.output(file_name, 'F')