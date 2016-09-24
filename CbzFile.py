import os.path
import shutil
import zipfile


class CbzFile(object):

    def __init__(self, filepath):
        self.file = zipfile.ZipFile(filepath)
        
    def extractAll(self):
        file_ext = os.path.basename(self.file.filename)
        new_folder = os.path.splitext(file_ext)[0]
        self.file.extractall(new_folder)    
        
        if(self.hasInternalFolder()):
            self.makeSingleFolder()
    
    def hasInternalFolder(self):
        str_file_ext = os.path.basename(self.file.filename)                  # filename.extension
        new_folder = os.path.splitext(str_file_ext)[0]                      # folder has the same name of file
        directory = os.path.dirname(self.file.filename) + '/' + new_folder   # path/folder

        return os.path.isdir(directory+'/'+os.listdir(directory)[0])
        
    def makeSingleFolder(self):
        
        str_file_ext = os.path.basename(self.file.filename)                  # filename.extension
        new_folder = os.path.splitext(str_file_ext)[0]                      # folder has the same name of file
        
        target = os.path.dirname(self.file.filename) + '/' + new_folder      
        source = target + '/' +os.listdir(target)[0]   
        
        files = os.listdir(source)
        
        for f in files:
            if (f.lower().endswith('png') or f.lower().endswith('jpg') or f.lower().endswith('jpeg')):
                shutil.move(source + '/' + f, target + '/' + f)
        
        shutil.rmtree(source)
        
    def test(self):
        pass