import os
import sys

#inheriting from exception
class HousingException(Exception):
#error_message is the object of exception and error_detail from which line error occured the sys module
    def __init__(self, error_message:Exception, error_detail:sys):
        """To identify the error where it occured and what type of error"""

        super().__init__(error_message)
        """ super()==Exception(error_message) that means the error
        message passed to the exception class"""

        self.error_message=error_message

    @staticmethod
    

    
      
    