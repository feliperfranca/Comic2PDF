class ComicFile(object):

    def __init__(self, strategy):
        self.strategy = strategy
        
    def extractAll(self):
        self.strategy.extractAll()
        
    def extractImages(self):
        self.strategy.extractImages()
        
    def test(self):
        self.strategy.test()
        