from . import regist
from . import transform
from . import checker
from_file=transform.from_file
from_string=transform.from_string
to_object=transform.to_object
reg=regist.reg

__all__=['reg','from_file','from_string','to_object']



