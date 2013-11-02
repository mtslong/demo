import operator
import UserList

def dump(data):
    print type(data), "=>",
    if operator.isCallable(data):
        print "CALLABLE",
    if operator.isMappingType(data):
        print "MAPPING",
    if operator.isNumberType(data):
        print "NUMBER",
    if operator.isSequenceType(data):
        print "SEQUENCE",
    print
        
dump(0)
dump("string")
dump("string"[0])
dump([1, 2, 3])
dump((1, 2, 3))
dump({"a": 1})
dump(len) # function
dump(UserList) # module
dump(UserList.UserList) # class
dump(UserList.UserList()) # instance

## <type 'int'> => NUMBER
## <type 'string'> => SEQUENCE
## <type 'string'> => SEQUENCE
## <type 'list'> => SEQUENCE
## <type 'tuple'> => SEQUENCE
## <type 'dictionary'> => MAPPING
## <type 'builtin_function_or_method'> => CALLABLE
## <type 'module'> =>
## <type 'class'> => CALLABLE
## <type 'instance'> => MAPPING NUMBER SEQUENCE
