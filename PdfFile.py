import os.path

from PIL import Image
from fpdf.fpdf import FPDF


class PdfFile(object):

    def __init__(self):
        self.pdf = None
    
        
    def getImageSize(self, image_filepath):
        with Image.open(image_filepath) as im:
            width, height = im.size
        
        return [width, height]
    
    
    def generatePdf(self, imagesFolder, pdfFilename):
        genericImageFilepath = imagesFolder + '/' + os.listdir(imagesFolder)[0]
        
        self.pdf = FPDF('P','pt',self.getImageSize(genericImageFilepath));
        
        for image in os.listdir(imagesFolder):
            self.pdf.add_page()
            self.pdf.image(imagesFolder + '/' + image, 0, 0)
            
        self.pdf.output( pdfFilename + '.pdf', "F")
        