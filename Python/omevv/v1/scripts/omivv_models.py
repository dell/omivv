from collections import namedtuple

class OMIVVConsole:
    def __init__(self,id,href,objectType,hostname,ip):
        self.id,self.href,self.objectType,self.hostname,self.ip = id,href,objectType,hostname,ip

    def __iter__(self):
        return iter([self.id, self.objectType, self.hostname,self.ip])

class OMIVVRepoProfile:
    def __init__(self,id,href,objectType,profileName,description,repoType):
        self.id,self.href,self.objectType,self.profileName,self.description,self.repoType = id,href,objectType,profileName,description,repoType
    def __iter__(self):
        return iter([self.id,self.href,self.objectType,self.profileName,self.description,self.repoType])

def consoleDecoder(consoleDict):
        return namedtuple('X', consoleDict.keys())(*consoleDict.values())

def repoProfileDecoder(profileDict):
    return namedtuple('X', profileDict.keys())(*profileDict.values())

def ClusterProfileDecoder(profileDict):
    return namedtuple('X', profileDict.keys())(*profileDict.values())
