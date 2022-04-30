from abc import ABC, abstractmethod

class DbAdapter(ABC):

    @abstractmethod
    def open_query(self,params,select="",procname=""):
        pass

    @abstractmethod
    def execute_statement(self,params,statement="",procname=""):
        pass