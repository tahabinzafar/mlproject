import sys
import logging

# This code essentially provides a mechanism to generate custom exceptions 
# with detailed error messages containing 
# information about the file name and line number where the exception occurred.

def error_message_details(error, error_detail:sys):

    _,_,exc_tb =error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(    
    file_name,exc_tb.tb_lineno,str(error))

    return error_message



class CustomException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message






    