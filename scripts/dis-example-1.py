import dis

def procedure():
    print 'hello'

dis.dis(procedure)

##           0 SET_LINENO          3
##
##           3 SET_LINENO          4
##           6 LOAD_CONST          1 ('hello')
##           9 PRINT_ITEM
##          10 PRINT_NEWLINE
##          11 LOAD_CONST          0 (None)
##          14 RETURN_VALUE
