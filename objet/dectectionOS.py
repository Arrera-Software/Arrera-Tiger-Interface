import platform

class OS :
    def __init__(self) :
        self.os = platform.system()
        
    def osWindows(self):
        if self.os == "Windows":
           return True
        else :
            return False
    
    def osLinux(self):
        if self.os == "Linux":
            return True
        else :
            return False
                