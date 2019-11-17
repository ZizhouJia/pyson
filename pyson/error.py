import antlr4
class CheckWrongError(Exception):
    def __init__(self,msg=None,location=None,line=None,column=None):
        self.msg=str(msg)+" at "+str(location)+" ("+str(line)+", "+str(column)+")"
    
    def __str__(self):
        return self.msg
    
    def set_msg(self,msg):
        self.msg=msg

class TransformWrongError(Exception):
    def __init__(self,msg=None,location=None,line=None,column=None,before_msg=None):
        self.msg=str(msg)+" at "+str(location)+" ("+str(line)+", "+str(column)+")"
        if(before_msg is not None):
            self.msg+=" reason for "
            self.msg+=before_msg
    
    def __str__(self):
        return self.msg
    
    def set_msg(self,msg):
        self.msg=msg

class ReigistError(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return str(self.msg)
    
    def set_msg(self,msg):
        self.msg=msg

class SyntaxErrorListener(antlr4.error.ErrorListener.ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("line "+str(line)+":"+str(column)+" "+msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

class PysonSyntaxError(Exception):
    def __init__(self,msg):
         self.msg=msg
    
    def __str__(self):
        return str(self.msg)
    
    def set_msg(self,msg):
        self.msg=msg