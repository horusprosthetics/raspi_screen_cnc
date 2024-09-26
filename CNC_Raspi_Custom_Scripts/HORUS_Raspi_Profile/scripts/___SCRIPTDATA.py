from ___EXCEPTION import SimCncException

class ScriptData:

    def __init__(self, dataString):
        self.dataParts = dataString.split(";")
        if not self.isCorrectDataPartsCount():
            raise SimCncException("Script data error - data parts count")

    def getCorrectDataPartsCount(self):
        return 3

    def isCorrectDataPartsCount(self):
        return len(self.dataParts) == self.getCorrectDataPartsCount()

    def getDataPart(self, index):
        return self.dataParts[index]

    def getPath(self):
        return self.getDataPart(0)

    def getAppNumber(self):
        return int(self.getDataPart(1))

    def getStartSource(self):
        return self.getDataPart(2)
