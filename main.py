import os.path
import shutil

from CbrFile import CbrFile
from CbzFile import CbzFile
from ComicFile import ComicFile
from PdfFile import PdfFile
import sys


if __name__ == '__main__':
        
    for filepath in sys.argv[1:]:
    
        comicFile = None
    
        ext = os.path.splitext(filepath)[1].lower()
        
        if   (ext == '.cbr' or ext == '.rar'):
            comicFile = ComicFile(CbrFile(filepath))
            comicFile.extractAll()
        elif (ext == '.cbz' or ext == '.zip'):
            comicFile = ComicFile(CbzFile(filepath))
            comicFile.extractAll()
        
        
        
        path, file  = os.path.split(filepath)
        filename, extention = os.path.splitext(file)
            
        imagesFolder = path + '/' + filename
        
        pdf = PdfFile()
        pdf.generatePdf(imagesFolder, filename)
    
        shutil.rmtree(imagesFolder, filename)