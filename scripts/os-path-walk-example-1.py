import os

def callback(arg, directory, files):
    for file in files:
        print os.path.join(directory, file), repr(arg)

os.path.walk(".", callback, "secret message")

## ./aifc-example-1.py 'secret message'
## ./anydbm-example-1.py 'secret message'
## ./array-example-1.py 'secret message'
## ...
## ./samples 'secret message'
## ./samples/sample.jpg 'secret message'
## ./samples/sample.txt 'secret message'
## ./samples/sample.zip 'secret message'
## ./samples/articles 'secret message'
## ./samples/articles/article-1.txt 'secret message'
## ./samples/articles/article-2.txt 'secret message'
## ...
