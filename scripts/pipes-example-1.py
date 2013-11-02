import pipes

t = pipes.Template()

# create a pipeline
t.append("sort", "--")
t.append("uniq", "--")

# filter some text
t.copy("samples/sample.txt", "")

## Alan Jones (sensible party)
## Kevin Phillips-Bong (slightly silly)
## Tarquin Fin-tim-lin-bin-whin-bim-lin-bus-stop-F'tang-F'tang-Olé-Biscuitbarrel
