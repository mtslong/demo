import whrandom

# initialize all generators with the same seed
rand1 = whrandom.whrandom(4,7,11)
rand2 = whrandom.whrandom(4,7,11)
rand3 = whrandom.whrandom(4,7,11)

for i in range(5):
    print rand1.random(), rand2.random(), rand3.random()

## 0.123993532536 0.123993532536 0.123993532536
## 0.180951499518 0.180951499518 0.180951499518
## 0.291924111809 0.291924111809 0.291924111809
## 0.952048889363 0.952048889363 0.952048889363
## 0.969794283643 0.969794283643 0.969794283643
