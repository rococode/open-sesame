import os
import io
from tqdm import tqdm
from nltk.tokenize import sent_tokenize

input_dir = "unsup/orig/"
output_dir = "unsup/split/"

if not os.path.exists(os.path.dirname(output_dir)):
    try:
        os.makedirs(os.path.dirname(output_dir))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

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
        print(split_lines)
        with io.open(os.path.join(output_dir, name), "w+", encoding='latin-1') as output:
            output.writelines(split_lines)

        #print(lines)
