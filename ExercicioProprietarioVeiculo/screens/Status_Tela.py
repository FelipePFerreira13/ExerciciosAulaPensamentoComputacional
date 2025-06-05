class Status_Tela():
    
    def __init__(self, status = 0):
        
        self.__status = status
        
    
    
    def get_status(self):
        return self.__status
     
    def set_status(self, novo):
        self.__status = novo