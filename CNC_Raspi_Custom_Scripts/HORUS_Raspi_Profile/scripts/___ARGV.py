import sys as simCncSys

class Argv:

    def getArg(self, index):
        return simCncSys.argv[index]

    def getProcessInstanceNumber(self):
        return int(self.getArg(1))

    def getSecretCode(self):
        return self.getArg(2)

    def getDebugId(self):
        return int(self.getArg(3))

    def getSimCncArgvLen(self):
        return 4

    def isSimCncArgvLen(self):
        return len(simCncSys.argv) == self.getSimCncArgvLen()

    def getSimCncSecretCode(self):
        return "Super secret code"

    def argumentsContainSecretCode(self):
        return self.getSecretCode() == self.getSimCncSecretCode()

    def isRunFromSimCnc(self):
        return self.isSimCncArgvLen() and self.argumentsContainSecretCode()
