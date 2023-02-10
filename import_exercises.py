import itertools as i

list_p = list(i.permutations('ABC',3))
print(list_p)
#6
list_c = list(i.combinations('ABCD',2))
print(list_c)
#3
list_per = list(i.permutations('ABCD',2))
print(list_per.count)

import json
json.load(open('profiles.json'))

#Pushing p