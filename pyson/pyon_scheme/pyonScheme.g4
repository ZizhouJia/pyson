grammar pyonScheme;
INT:[+-]?[0-9]+;
FLOAT:[-+]?([0-9]+('.'[0-9]*)?|'.'[0-9]+)([eE][-+]?[0-9]+)?;
TRUE: 'True'|'true';
FALSE: 'False'|'false';
NONE: 'None'|'none';
KEY: [A-Za-z_]+[A-Za-z0-9_]*;
fragment ESC_DOUBLE : '\\"' ;
fragment ESC_SINGLE : '\\\'';
STRING: '"' (ESC_DOUBLE|.|'\\' [btnr"\\])*?'"'|'\'' (ESC_SINGLE|.|'\\' [btnr"\\])*? '\'' ;
OBJECT: ([A-Za-z_]+[A-Za-z0-9_]*)?'@'(([A-Za-z_]+[A-Za-z0-9_]*|'0'|[1-9][0-9]*|'*')'.')*([A-Za-z_]+[A-Za-z0-9_]*|'0'|'*'|[1-9][0-9]*);
CHECKER: ([A-Za-z_]+[A-Za-z0-9_]*)?'#'(([A-Za-z_]+[A-Za-z0-9_]*|'0'|[1-9][0-9]*)'.')*([A-Za-z_]+[A-Za-z0-9_]*|'0'|[1-9][0-9]*);
COLON: ',';
COMMA: ':';
DOT: '.';

LEFT_DICT:'{';
RIGHT_DICT:'}';
LEFT_LIST:'[';
RIGHT_LIST:']';
LEFT_BUKKET:'(';
RIGHT_BUKKET:')';
LINE_COMMENT  : '//' .*? '\r'? '\n' -> skip ;
COMMENT       : '/*' .*? '*/' ->skip ; 
WS : [ \t\r\n]+ -> skip ;

entry_point:OBJECT checker_dict;
checker_dict:LEFT_DICT items RIGHT_DICT;
items: item other_items|; 
other_items: COLON item other_items|;
item: KEY COMMA value; //the object value
value: checker_dict| checker_object;
checker_object: CHECKER (variable_dict|);
list_items: variable_item other_variable_items|;
other_variable_items: COLON variable_item other_variable_items|;
variable_item:INT|FLOAT|TRUE|FALSE|NONE|STRING|OBJECT|checker_object|variable_list;
variable_list: LEFT_LIST list_items RIGHT_LIST;
variable_dict: LEFT_DICT variable_dict_items RIGHT_DICT;
variable_dict_items: variable_dict_item other_variable_dict_items|;
other_variable_dict_items: COLON variable_dict_item other_variable_dict_items|;
variable_dict_item: KEY COMMA variable_item;






