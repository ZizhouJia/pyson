grammar pyon;
INT:[+-]?[0-9]+;
FLOAT:[-+]?([0-9]+('.'[0-9]*)?|'.'[0-9]+)([eE][-+]?[0-9]+)?;
TRUE: 'True'|'true';
FALSE: 'False'|'false';
NONE: 'None'|'none';
CTX:'ctx';
KEY: [A-Za-z_]+[A-Za-z0-9_]*;
fragment ESC_DOUBLE : '\\"' ;
fragment ESC_SINGLE : '\\\'';
STRING: '"' (ESC_DOUBLE|.|'\\' [btnr"\\])*?'"'|'\'' (ESC_SINGLE|.|'\\' [btnr"\\])*? '\'' ;
OBJECT: ([A-Za-z_]+[A-Za-z0-9_]*)?'@'(([A-Za-z_]+[A-Za-z0-9_]*|'0'|[1-9][0-9]*)'.')*([A-Za-z_]+[A-Za-z0-9_]*|'0'|[1-9][0-9]*);
COLON: ',';
COMMA: ':';
LEFT_DICT:'{';
RIGHT_DICT:'}';
LEFT_LIST:'[';
RIGHT_LIST:']';
LEFT_BUKKET:'(';
RIGHT_BUKKEFT:')';
LINE_COMMENT  : '//' .*? '\r'? '\n' -> skip ;
COMMENT       : '/*' .*? '*/' ->skip ; 
WS : [ \t\r\n]+ -> skip ;
entry_point: item_dict;
item_dict: LEFT_DICT items RIGHT_DICT;
items: item other_items|; 
other_items: COLON item other_items|;
item: KEY COMMA value;
value: INT|FLOAT|TRUE|FALSE|NONE|STRING|CTX|item_dict|item_list|item_object;
values: value other_values|;
other_values: COLON value other_values|;   
item_list: LEFT_LIST values RIGHT_LIST;
item_tuple:LEFT_BUKKET values RIGHT_BUKKEFT;
item_object: OBJECT (item_dict|item_tuple|);





