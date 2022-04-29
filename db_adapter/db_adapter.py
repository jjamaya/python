from abc import ABC, abstractmethod

class DbAdapter(ABC):

    @abstractmethod
    def open_procedure(self,procname,params):
        pass

    @abstractmethod
    def execute_procedure(self,procname,params):
        pass



