import re 
import math

with open("Data/d03/real.txt") as f:
        input = [f"{'.'}{i}{'.'}" for i in f.read().split("\n")]

nrows = len(input)
sum_mod = 0
dict = {}

for ii in range(len(input)):
    ori = input[ii]
    mod = [re.sub('\D', '', o) for o in re.split('\D+', ori) if re.sub('\D', '', o) != ""]
    ind = []
    track = 0
    for n in range(len(ori)):
        track += 1
        if ori[n].isdigit():
            ind.append(n)
        else:
            ind.append(None)
    ind = [i for i, j in zip(ind, [None] + ind) if i is not None and j is None]
    if len(mod) == 0:
        continue
    for jj in range(len(mod)):
        indx = ind[jj]
        mlen = len(mod[jj])
        up = input[max(ii - 1, 0)][(indx - 1):(indx + mlen + 1)]
        dwn = input[min(ii + 1, nrows - 1)][(indx - 1):(indx + mlen + 1)]
        mid = ori[(indx - 1):(indx + mlen + 1)]
        cat = up + mid + dwn
        if re.search('[^0-9.]', cat):
            sum_mod += int(mod[jj])
            # finding *
            if "*" in up:
                indices = [i for i, x in enumerate(up) if x == '*']
                for indice in indices:
                    s = f"{indice + indx - 1},{ii - 1}"
                    if s not in dict:
                        dict[s] = []
                    dict[s].append(str(mod[jj]))
            if "*" in dwn:
                indices = [i for i, x in enumerate(dwn) if x == '*']
                for indice in indices:
                    s = f"{indice + indx - 1},{ii + 1}"
                    if s not in dict:
                        dict[s] = []
                    dict[s].append(str(mod[jj]))
            if "*" in mid:
                indices = [i for i, x in enumerate(mid) if x == '*']
                for indice in indices:
                    s = f"{indice + indx - 1},{ii}"
                    if s not in dict:
                        dict[s] = []
                    dict[s].append(str(mod[jj]))

prod_mod = 0
for k, v in dict.items():
    if len(v) > 1:
        prod_mod += math.prod([int(i) for i in v])


for i, ans in enumerate([sum_mod, prod_mod]):
        print(f"Part {i + 1} answer: {ans}")
