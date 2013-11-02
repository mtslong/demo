import sunaudio

file = "samples/sample.au"

print sunaudio.gethdr(open(file, "rb"))

## (6761, 1, 8012, 1, 'sample.au')
