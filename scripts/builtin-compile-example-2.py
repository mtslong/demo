BODY = """
print 'the ant, an introduction'
"""

code = compile(BODY, "<script>", "exec")

print code

exec code

## <code object ? at 8c6be0, file "<script>", line 0>
## the ant, an introduction
