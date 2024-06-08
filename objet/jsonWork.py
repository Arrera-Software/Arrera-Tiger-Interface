import json
import requests

class jsonWork : 
    def __init__(self):
        self.fichier = str 
        self.contenuJson = str
        self.__onlineFile = bool
        self.__localFile = bool
    
    def __reloadFile(self):
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__readFile.close()
            self.__readFile = open(self.fichier, 'r', encoding='utf-8')
            self.__readFile.seek(0)  # Rembobiner le fichier au début
            self.contenuJson = json.load(self.__readFile)
        
    def loadFile(self, fichier: str):
        self.fichier = fichier
        self.__readFile =  open(fichier, 'r', encoding='utf-8') 
        self.contenuJson = json.load(self.__readFile)
        self.__localFile=True
        self.__onlineFile=False
    
    def loadInternet(self,url:str):
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.contenuJson = response.json()
            self.__localFile=False
            self.__onlineFile=True
        except requests.exceptions.RequestException as e:
            self.__localFile=False
            self.__onlineFile=False
        
    def __openWrite(self):
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__writeFile = open(self.fichier,"w")
        
    def lectureJSON(self,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction
        if ((self.__localFile==True) or (self.__onlineFile==True)):
            dict = self.contenuJson[flag]
            return str(dict)
        else :
            return "error"
    
    def lectureJSONMultiFlag(self,flag1,flag2):
        if ((self.__localFile==True) or (self.__onlineFile==True)):
            dict = self.contenuJson[flag1][flag2]
            return str(dict)
        else :
            return "error"
    
    def lectureJSONList(self,flag):
        if ((self.__localFile==True) or (self.__onlineFile==True)):
            liste = self.contenuJson[flag]
            return list(liste)
        else :
            return ["aaaa","aaa"]
    
    def lectureJSONDict(self,flag):
        if ((self.__localFile==True) or (self.__onlineFile==True)):
            dictionnaire = self.contenuJson[flag]
            return dict(dictionnaire)
        else :
            return {"aaaaa":"aaaa","aaaaa":"aaaa","aaaaa":"aaaa"} 
    
    def EcritureJSON(self,flag,valeur):#Permet d'ecrire une nouvelle valeur a flag definie
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__openWrite()
            self.contenuJson[flag] = valeur
            json.dump(self.contenuJson,self.__writeFile,indent=2)
            self.__writeFile.close()
            self.__reloadFile()
            return True
        else :
            return False
        
    def EcritureJSONList(self, flag, valeur):
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__openWrite()
            if flag in self.contenuJson and isinstance(self.contenuJson[flag], list):
                # Ajoutez la nouvelle valeur à la liste
                self.contenuJson[flag].append(valeur)
                # Écrivez le fichier JSON mis à jour
                json.dump(self.contenuJson, self.__writeFile, indent=2)
            self.__writeFile.close()
            self.__reloadFile()
            return True
        else :
            return False
        
    def EcritureJSONDictionnaire(self, flag, cle, valeur):
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__openWrite()
            if flag in self.contenuJson and isinstance(self.contenuJson[flag], dict):
                self.contenuJson[flag][cle] = valeur  # Met à jour le dictionnaire
                json.dump(self.contenuJson, self.__writeFile, indent=2)
            self.__writeFile.close()
            self.__reloadFile()
            return True
        else :
            return False
    
    def supprJSONDict(self, flag, cle):
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__openWrite()
            if flag in self.contenuJson and isinstance(self.contenuJson[flag], dict):
                if cle in self.contenuJson[flag]:
                    del self.contenuJson[flag][cle]  # Supprime la clé spécifiée du dictionnaire
                    json.dump(self.contenuJson,self.__writeFile, indent=2)
            self.__writeFile.close()
            self.__reloadFile()    
            return True
        else :
            return False
                    
    
    def suppressionJson(self, flag:str):
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__openWrite()
            if flag in self.contenuJson:
                self.contenuJson[flag]="" # Supprime le champ spécifié
                json.dump(self.contenuJson, self.__writeFile, indent=2)
            self.__writeFile.close()
            self.__reloadFile()
            return True
        else :
            return False
    
    def suppressionJsonList(self, flag, valeur):
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__openWrite()
            if flag in self.contenuJson and isinstance(self.contenuJson[flag], list):
                liste = self.contenuJson[flag]
                if valeur in liste:
                    liste.remove(valeur)  # Supprime la valeur spécifiée de la liste
                    json.dump(self.contenuJson, self.__writeFile, indent=2)
            self.__writeFile.close()
            self.__reloadFile()
            return True
        else :
            return False

    def dictJson(self):
        return self.contenuJson
       
    def compteurFlagJSON(self):
        return len(self.contenuJson)
    
    def supprDictReorg(self,flag):  
        if ((self.__localFile==True) and (self.__onlineFile==False)):
            self.__openWrite()
            del self.contenuJson[flag]
            newDict = {}
            newKey = 0
            for cle in sorted(self.contenuJson.keys(), key=lambda x: int(x)):
                newDict[str(newKey)] = self.contenuJson[cle]
                newKey += 1
            json.dump(newDict,self.__writeFile,indent=2)
            self.__writeFile.close()
            self.__reloadFile()
            return True
        else :
            return False