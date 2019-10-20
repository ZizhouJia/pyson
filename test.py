import pyson
result=pyson.from_file("input.pyon")
print(result)
result=pyson.to_object(result)
print(result[0])