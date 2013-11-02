import random

for i in range(5):

    # random float: 0.0 <= number < 1.0
    print random.random(),

    # random float: 10 <= number < 20
    print random.uniform(10, 20),

    # random integer: 100 <= number <= 1000
    print random.randint(100, 1000),

    # random integer: even numbers in 100 <= number < 1000
    print random.randrange(100, 1000, 2)

## 0.946842713956 19.5910069381 709 172
## 0.573613195398 16.2758417025 407 120
## 0.363241598013 16.8079747714 916 580
## 0.602115173978 18.386796935 531 774
## 0.526767588533 18.0783794596 223 344
