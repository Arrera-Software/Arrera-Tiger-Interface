from objet.jsonWork import*
import urllib.request
from objet.dectectionOS import*
import zipfile
import os


class CArreraTiger :
    def __init__(self,url:str) :
        self.__json = jsonWork()
        self.__system = OS()
        self.__json.loadInternet(url)
    
    def install(self,soft:str,fileName,emplacemntSoft):
        linux = self.__system.osLinux()
        windows = self.__system.osWindows()
        if ((linux==False) and (windows == True)):
            link = self.__json.lectureJSONMultiFlag("windows",soft)
        else :
            if ((linux==True) and (windows == False)):
                link = self.__json.lectureJSONMultiFlag("linux",soft)
            else :
                return -1
        urllib.request.urlretrieve(link,fileName)  
        sortie = self.__unzip(fileName,emplacemntSoft)
        if sortie==False :
            return -2 
        else : 
            return 0
    
    def listSoft(self)->list:
        linux = self.__system.osLinux()
        windows = self.__system.osWindows()
        if ((linux==False) and (windows == True)):
            return list(self.__json.lectureJSONDict("windows").keys())
        else :
            if ((linux==True) and (windows == False)):
                return list(self.__json.lectureJSONDict("linux").keys())
            else :
                return "errror"

    def __unzip(self,zipFile, floder):
        if not os.path.exists(zipFile):
            return False
        if not os.path.exists(floder):
            os.makedirs(floder)
        with zipfile.ZipFile(zipFile, 'r') as zip_ref:
            zip_ref.extractall(floder)
            self.__delFile(zipFile)
            return True   
    
    def __delFile(self,file_path):
        try:
            os.remove(file_path)
            return 0
        except FileNotFoundError:
            return 1
        except PermissionError:
            return 2
        except Exception as e:
            return 3 
    
    def getJsonObjet(self):
        return self.__json