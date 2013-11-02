def dump(expression):
    result = eval(expression)
    print expression, "=>", result, type(result)

dump("1")
dump("1.0")
dump("'string'")
dump("1.0 + 2.0")
dump("'*' * 10")
dump("len('world')")

## 1 => 1 <type 'int'>
## 1.0 => 1.0 <type 'float'>
## 'string' => string <type 'string'>
## 1.0 + 2.0 => 3.0 <type 'float'>
## '*' * 10 => ********** <type 'string'>
## len('world') => 5 <type 'int'>
