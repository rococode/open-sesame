import os
import io
from tqdm import tqdm
from nltk.tokenize import sent_tokenize

input_dir = "unsup/orig/"
output_dir = "unsup/split/"

def create_dir(name):
    if not os.path.exists(os.path.dirname(name)):
        try:
            os.makedirs(os.path.dirname(name))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
create_dir(output_dir)
for i in range(1, 11):
    create_dir(output_dir + str(i) + "/")

idx = 1
curr = 0
step = 5000

for name in tqdm(os.listdir(input_dir)):
    with io.open(os.path.join(input_dir, name), "r", encoding='latin-1') as file:
        lines = file.readlines()
        tmp = []
        for line in lines:
            tmp.extend(line.split("<br />"))
        lines = tmp;
        split_lines = []
        for line in lines:
            tokenized = sent_tokenize(line)
            split_lines.extend(tokenized)
        for x in split_lines:
            if len(x) == 0:
                split_lines.remove(x)
        #split_lines = [x.encode("latin-1") + "\n" for x in split_lines]
        split_lines = [x + "\n" for x in split_lines]
        #for x in split_lines:
        #    print(x, type(x))
        split_lines = [x.encode("ascii", "replace").decode() for x in split_lines]
        #for x in split_lines:
        #    print(x, type(x))
        #import sys;sys.exit(0)
        # print(split_lines)
        with io.open(os.path.join(output_dir + str(idx) + "/", name), "w+") as output:
            output.writelines(split_lines)
    curr = curr + 1
    if curr >= step:
        curr = 0
        idx = idx + 1

        #print(lines)
