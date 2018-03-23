from collections import Counter
from hashlib import md5

path = './book.txt'

def chunkify(inputfile):
    with open(inputfile, 'r') as file:
        while True:
            buffer = file.read(10240)
            if not buffer:
                break

            # make sure we end on a space (word boundary)
            while not str.isspace(buffer[-1]):
                char = file.read(1)
                if not char:
                    break
                buffer += char

            yield buffer
        yield '' #handle the scene that the file is

def text_counter(text):
    counter = Counter()
    for line in text.splitlines():
        counter.update(line.split())
    return counter

master_counter = Counter()

for text in chunkify(path):
    master_counter += text_counter(text)

print(master_counter.most_common(10))