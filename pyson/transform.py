from . import regist
from . import pyon
from antlr4 import *


def intable(content):
    try:
        int(content)
        return True
    except:
        return False


class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)
    
        
    def _extract_obj_string(self,prefix,value,stored_dict):
        if(value is None):
            stored_dict[prefix]=("None","None")
            return
        if(isinstance(value,obj)):
            for key,v in vars(value).items():
                self._extract_obj_string(prefix+"."+str(key),v,stored_dict)
            return
        if(isinstance(value,list)):
            for i in range(0,len(value)):
                self._extract_obj_string(prefix+"."+str(i+1),value[i],stored_dict)
            return
        stored_dict[prefix]=(type(value),str(value))

    def __str__(self):
        stored_dict={}
        output_string=""
        for key,value in vars(self).items():
            self._extract_obj_string(key,value,stored_dict)
        for key,value in stored_dict.items():
            output_string+=key
            output_string+=":("
            output_string+=str(value[0])+","+value[1]+")\n"
        return output_string


class transformer(object):
    def __init__(self,reg):
        self.reg=reg
    
    def _get_object(self,object_name,root_store):
        scope,others=regist.object_name_utils.split_scope_name(object_name)
        if(scope!="self"):
            return self.reg.get_object(object_name)
        else:
            others=others.split('.')
            current_node=root_store
            for i in range(0,len(others)):
                if(intable(others[i])):
                    if(isinstance(current_node,list)):
                        current_node=current_node[int(others[i])]
                        continue
                    else:
                        return None
                else:
                    if(isinstance(current_node,dict)):
                        if(others[i] in current_node.keys()):
                            current_node=current_node[others[i]]
                            continue
                        else:
                            return None
                return False
            return (current_node,None)
    
    def _transform_list(self,pyon_object,current_store,root_store):
        for i in range(0,len(pyon_object)):
            if(isinstance(pyon_object[i],(int,float,bool,str))):
                current_store.append(pyon_object[i])
                continue
            if(isinstance(pyon_object[i],tuple)):
                store=[]
                self._transform_object(pyon_object[i],store,root_store)
                current_store.append(store[0])
                continue
            if(isinstance(pyon_object[i],list)):
                store=[]
                current_store.append(store)
                self._transform_list(pyon_object[i],store,root_store)
                continue
            if(isinstance(pyon_object[i],dict)):
                store={}
                current_store.append(store)
                self._transform_dict(pyon_object[i],store,root_store)
                continue

    def _transform_dict(self,pyon_object,current_store,root_store):
        for key,value in pyon_object.items():
            if(isinstance(pyon_object[key],(int,float,bool,str))):
                current_store[key]=value
                continue
            if(isinstance(pyon_object[key],tuple)):
                store=[]
                self._transform_object(pyon_object[key],store,root_store)
                current_store[key]=store[0]
                continue
            if(isinstance(pyon_object[key],list)):
                store=[]
                current_store[key]=store
                self._transform_list(pyon_object[key],store,root_store)
                continue
            if(isinstance(pyon_object[key],dict)):
                store={}
                current_store[key]=store
                self._transform_dict(pyon_object[key],store,root_store)
                continue


    def _transform_object(self,pyon_object,current_store,root_store):
        if(pyon_object[0]=="ctx"):
            current_store.append(root_store)
            return
        obj_class=self._get_object(pyon_object[0],root_store)
        if(obj_class is None):
            raise RuntimeError("The "+pyon_object[0]+" can not be found")
        if(pyon_object[1] is None):
            current_store.append(obj_class[0])
            return
        try:
            if(isinstance(pyon_object[1],list)):
                params_list=[]
                self._transform_list(pyon_object[1],params_list,root_store)
                obj=obj_class[0](*params_list)
                current_store.append(obj)
                return
            if(isinstance(pyon_object[1],dict)):
                params={}
                self._transform_dict(pyon_object[1],params_dict,root_store)
                if(code is False):
                    return code,reason
                obj=obj_class[0](**params)
                current_store.append(obj)
                return
        except:
            raise RuntimeError("The params for object "+pyon_object[0]+" is wrong")


    def transfrom(self,pyon_obj):
        if(isinstance(pyon_obj,dict)):
            root_store={}
            current_store=root_store
            self._transform_dict(pyon_obj,current_store,root_store)
            return root_store
        if(isinstance(pyon_obj,list)):
            root_store=[]
            current_store=root_store
            self._transform_list(pyon_obj,current_store,root_store)
            return root_store
        else:
            return None

            

reg=regist.reg
trans=transformer(reg)

def from_file(file_name):
    input=FileStream(file_name,encoding='utf-8')
    lexer=pyon.pysonLexer.pysonLexer(input)
    token_stream=CommonTokenStream(lexer)
    parser=pyon.pysonParser.pysonParser(token_stream)
    tree=parser.entry_point()
    listener=pyon.pysonListener.pysonListener()
    # tree_str=tree.toStringTree(recog=parser)
    walker=ParseTreeWalker()
    walker.walk(listener,tree)
    d=listener.return_value
    result=trans.transfrom(d)
    return result

def from_string(pyson_string):
    input=InputStream(pyson_string)
    lexer=pyon.pysonLexer.pysonLexer(input)
    token_stream=CommonTokenStream(lexer)
    parser=pyon.pysonParser.pysonParser(token_stream)
    tree=parser.entry_point()
    listener=pyon.pysonListener.pysonListener()
    walker=ParseTreeWalker()
    walker.walk(listener,tree)
    d=listener.return_value
    result=trans.transfrom(d)
    return result

def to_object(pyson_obj):
    obj_dict={}
    obj_dict["pyson_obj"]=pyson_obj
    python_obj=obj(obj_dict)
    return python_obj.pyson_obj


