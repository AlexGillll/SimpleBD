import json
import os

class My_simple_bd(object):
    def __init__(self, location):
        '''mydb = My_simple_bd("./mydb.db")'''
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.bd = {}
        return True

    def _load(self):
        self.bd = json.load(open(self.location, 'r'))

    def dumpbd(self):
        try:
            json.dump(self.bd, open(self.location, 'w+'))
            return True
        except:
            False

    def set(self, key, value):
        #mydb.set("name" , "Sasha") #Sets Value
        try:
            self.bd[str(key)] = value
            self.dumpbd()
        except Exception as e:
            print('[X] Error Saving Values to Database : ' + str(e))
            return False

    def get(self, key):
        #mydb.get("name") --> 'Sasha'
        try:
            return self.bd[key]
        except KeyError:
            print("No Value can be found for " + str(key))
            return False
        
    def delete(self, key):
        if not key in self.bd:
            return False
        del self.bd[key]
        self.dumpbd()
        return True

    def resetBd(self):
        self.bd = {}
        self.dumpbd()
        return True



