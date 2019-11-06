import antlr4
class CheckWrongError(Exception):
    def __init__(self,msg,location,line,column):
        self.msg=msg
        self.location=location
        self.line=line
        self.column=column
    
    def __str__(self):
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

class ReigistError(Exception):
    def __init__(self,msg):
        self.msg=msg

    def str(self):
        return str(self.msg)

class SyntaxErrorListener(antlr4.error.ErrorListener.ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("line "+str(line)+":"+str(column)+" "+msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

class SyntaxError(Exception):
    def __init__(self,msg):
         self.msg=msg
    
    def __str__(self):
        return str(self.msg)