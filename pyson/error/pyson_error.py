class CheckWrongError(Exception):
    def __init__(self,msg,location,line,column):
        self.msg=msg
        self.location=location
        self.line=line
        self.column=column
    
    def str(self):
        return_value=self.location+":"+self.msg+" at ("+str(self.line)+","+str(self.column)+")"
        return str(return_value)

class TransformWrongError(Exception):
    def __init__(self,msg,location,line,column):
        self.msg=msg
        self.location=location
        self.line=line
        self.column=column
    
    def str(self):
        return_value=self.location+":"+self.msg+" at ("+str(self.line)+","+str(self.column)+")"
        return str(return_value)