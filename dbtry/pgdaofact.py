from DAOFact import *
from pguserdao import *

class pgdaofact(DAOFact):

    __instance = None

    def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
          raise Exception("This class is a singleton!")
      else:
          Singleton.__instance = self

    def getfact():
        if pgdaofact.__instance == None:
            pgdaofact()
        return pgdaofact.__instance


    def getuserdao():
        
        return pguserdao()
