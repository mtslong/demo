import htmlentitydefs

entities = htmlentitydefs.entitydefs

for entity in "amp", "quot", "copy", "yen":
    print entity, "=", entities[entity]

## amp = &
## quot = "
## copy = ©
## yen = ¥
