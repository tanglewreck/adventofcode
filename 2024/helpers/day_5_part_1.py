# coding: utf-8
rules = {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 29], 29: [13], 53: [29, 13]}
rules_str = """47:53
97:13
97:61
97:47
75:29
61:13
75:53
29:13
97:29
53:29
61:53
97:53
61:29
47:13
75:47
97:75
47:61
75:61
47:29
75:13
53:13
"""
rules_str
rules_str.split("\n")
rules_list = rules_str.split("\n")
[x.split(":") for x in rules_list]
[x.split(":") for x in rules_list][:-1]
for rule in [x.split(":") for x in rules_list][:-1]:
    print(rule)
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    if rule[0] not in rules_dict:
        rules_dict[rule[0]: [rule[1]]
    else:
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    if rule[0] not in rules_dict:
        rules_dict[rule[0]: rule[1]]
    else:
        rules_dict[rule[0]].append(rule[1])
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    print(rule)
#    if rule[0] not in rules_dict:
#        rules_dict[rule[0]: rule[1]]
#    else:
#        rules_dict[rule[0]].append(rule[1])
rules_dict
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    print(rule[0], rule[1])
#    if rule[0] not in rules_dict:
#        rules_dict[rule[0]: rule[1]]
#    else:
#        rules_dict[rule[0]].append(rule[1])
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    print(rule[0], rule[1])
#    if rule[0] not in rules_dict:
#        rules_dict[rule[0]: rule[1]]
#    else:
#        rules_dict[rule[0]].append(rule[1])
rules_dict["47" : ["53]] 
rules_dict[47 : [53]]
rules_dict[47] = [53]
rules_dict
47 in rules_dict
53 in rules_dict
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    print(rule[0], rule[1])
    if rule[0] not in rules_dict:
        rules_dict[int(rule[0])] = int(rule[1])
    else:
        rules_dict[int(rule[0])].append(int(rule[1]))
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
#    print(rule[0], rule[1])
    if rule[0] not in rules_dict:
        rules_dict[int(rule[0])] = int(rule[1])
    else:
        rules_dict[int(rule[0])].append(int(rule[1]))
rules_dict
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    print(int(rule[0]), (rule[1]))
    if rule[0] not in rules_dict:
        rules_dict[int(rule[0])] = int(rule[1])
    else:
        rules_dict[int(rule[0])].append(int(rule[1]))
rules_dict
rules_dict = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    print(rule[0], rule[1])
    if rule[0] not in rules_dict:
        rules_dict[rule[0]] = [rule[1]]
    else:
        rules_dict[rule[0]].append(rule[1])
rules_dict
rules
page_ordering = rules_dict
updates = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75,97,47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]
[str(x) for update in updates for x in update]
[str(x) for x in updates[0]]
[[str(x) for x in updates[0]] for update in updates]
[[str(x) for x in updates[0]] for update in updates]
updates
updates_raw = updates.copy()
[[str(x) for x in updates[0]] for update in updates]
[[str(x) for x in updates[0]] for update in updates_raw]
updates = [[str(x) for x in updates[0]] for update in updates_raw]
updates
rules
page_orderings = {}
for rule in [x.split(":") for x in rules_list][:-1]:
    print(rule[0], rule[1])
    if rule[0] not in page_orderings:
        page_orderings[rule[0]] = [rule[1]]
    else:
        page_orderings[rule[0]].append(rule[1])
page_orderings
updates
order = page_orderings.copy()
order
updates
'75' > ' 61'
updates_raw
[[str(x) for x in updates[0]] for update in updates_raw]
[str(x) for update in updates for update in updates_raw]
[str(x) for update in updates_raw for x in update]
for update in updates:
    print(len(update))
updates
updates_raw
for update in updates_raw:
    print(len(update))
[update for update in updates_raw]
[update for update in updates_raw]
len(updates_raw)
for x
u = []
for update in updates_raw:
    print(update)
type(updates_raw[0][0])
rules
order
page_orderings
rules
updates
updates_raw
rules
#updates = updates_raw.copy()
updates_raw
rules
updates = updates_raw.copy()
for update in updates:
    print(update)
rules
import defaultdict
import collections import defaultdict
from collections import defaultdict
help(defaultdict)
d = defaultdict()
d["foo"] = 1
d
d["bar"] = 2
d
d["foo"]
updates
d = defaultdict()
for update in updates:
    for x in update:
        d[x] += 1
d = defaultdict()
for update in updates:
    for x in update:
        d[x] = 0
d
d = defaultdict()
for update in updates:
    for x in update:
        d[x] += 1
d = defaultdict()
for update in updates:
    for x in update:
        d[x] = 0
for update in updates:
    for x in update:
        d[x] += 1
d
rules
rules.keys()
for rule in rules
d = defaultdict()
d = defaultdict()
for rule in rules.keys():
    d[rule] = 0
d
for update in updates:
    for x in update:
        d[x] += 1
rules
rules[13] =[]
rules
updates
rules[47]
97 in rules[47]
75 in rules[47]
75 in rules[61]
75 in rules[53]
for u in updates[0]:
    print(u)
for i, u in enumerate(updates[0]):
    print(i, u)
for i, u in enumerate(updates[0]):
    for j in range(i, len(updates[0])):
        print(j)
for i, u in enumerate(updates[0]):
    for j in range(i, len(updates[0])):
        print(j)
    print()
for i, u in enumerate(updates[0]):
    for j in range(i, len(updates[0])):
        print(j in rules[i])
    print()
rules
for i, u in enumerate(updates[0]):
    for j in range(i, len(updates[0])):
        print(j)
    print()
for i, u in enumerate(updates[0]):
    for j in range(i, len(updates[0])):
        print(j, u)
    print()
for i, u in enumerate(updates[0]):
    n = len(updates[0])
    for j in updates[0][i+1:n]:
        print(j, u)
    print()
updates[0]
for i, u in enumerate(updates[0]):
    n = len(updates[0])
    for j in updates[0][i+1:n]:
        print(u, j)
    print()
updates[0]
for i, u in enumerate(updates[0]):
    n = len(updates[0])
    for j in updates[0][i+1:n]:
        print(j in rules[u])
    print()
for i, u in enumerate(updates[0]):
    n = len(updates[0])
    for j in updates[0][i+1:n]:
        print(u, j in rules[u])
    print()
for i, u in enumerate(updates[0]):
    n = len(updates[0])
    for j in updates[0][i+1:n]:
        print(u, j, j in rules[u])
    print()
k = -1
for i, u in enumerate(updates[k]):
    n = len(updates[k])
    for j in updates[k][i+1:n]:
        print(u, j, j in rules[u])
    print()
k = -1
ok = True
for i, u in enumerate(updates[k]):
    n = len(updates[k])
    for j in updates[k][i+1:n]:
        print(u, j, j in rules[u])
        ok = j in rules[u]
    print()
print(f"ok = {ok}")
k = -1
ok = True
for i, u in enumerate(updates[k]):
    n = len(updates[k])
    for j in updates[k][i+1:n]:
#        print(u, j, j in rules[u])
        ok = j in rules[u]
    print()
print(f"ok = {ok}")
k = 0
ok = True
for i, u in enumerate(updates[k]):
    n = len(updates[k])
    for j in updates[k][i+1:n]:
#        print(u, j, j in rules[u])
        ok = j in rules[u]
    print()
print(f"ok = {ok}")
k = 0
ok = True
for i, u in enumerate(updates[k]):
    n = len(updates[k])
    for j in updates[k][i+1:n]:
#        print(u, j, j in rules[u])
        ok = j in rules[u]
#    print()
print(f"ok = {ok}")
k = 0
ok = True
for i, u in enumerate(updates[k]):
    n = len(updates[k])
    for j in updates[k][i+1:n]:
#        print(u, j, j in rules[u])
        ok = j in rules[u]
#    print()
print(f"update[k] = {ok}")
k = 0
ok = True
for i, u in enumerate(updates[k]):
    n = len(updates[k])
    for j in updates[k][i+1:n]:
#        print(u, j, j in rules[u])
        ok = j in rules[u]
#    print()
print(f"update[{k}] = {ok}")
k = 0
for k in range(len(updates)):
    ok = True
    for i, u in enumerate(updates[k]):
        n = len(updates[k])
        for j in updates[k][i+1:n]:
    #        print(u, j, j in rules[u])
            ok = j in rules[u]
    #    print()
    print(f"update[{k}] = {ok}")
k = 0
all_ok = True
for k in range(len(updates)):
    ok = True
    for i, u in enumerate(updates[k]):
        n = len(updates[k])
        for j in updates[k][i+1:n]:
    #        print(u, j, j in rules[u])
            ok = j in rules[u]
            if not ok:
                all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
for k in range(len(updates[0:2])):
    ok = True
    for i, u in enumerate(updates[k]):
        n = len(updates[k])
        for j in updates[k][i+1:n]:
    #        print(u, j, j in rules[u])
            ok = j in rules[u]
            if not ok:
                all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
for k in range(len(updates[0:3])):
    ok = True
    for i, u in enumerate(updates[k]):
        n = len(updates[k])
        for j in updates[k][i+1:n]:
    #        print(u, j, j in rules[u])
            ok = j in rules[u]
            if not ok:
                all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
for k in range(len(updates[0:3])):
    ok = True
    for i, u in enumerate(updates[k]):
        n = len(updates[k])
        for j in updates[k][i+1:n]:
    #        print(u, j, j in rules[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
for k, update in enumerate(updates):
    ok = True
    for i, u in enumerate(updates):
        n = len(update)
        for j in update[k][i+1:n]:
    #        print(u, j, j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
for k, update in enumerate(updates):
    ok = True
    for i, u in enumerate(update):
        n = len(update)
        for j in update[k][i+1:n]:
    #        print(u, j, j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
list(enumerate(updates))
list(enumerate(updates[0]))
k = 0
all_ok = True
for k, update in enumerate(updates):
    ok = True
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
    #        print(u, j, j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
for k, update in enumerate(updates[0:3]):
    ok = True
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
    #        print(u, j, j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[3:N]):
    ok = True
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
    #        print(u, j, j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
    #        print(u, j, j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            print(u, j, j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            print(u, j)  # , j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
    #    print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            print(u, j)  # , j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
        print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    print(f"update[{k}]")
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            print(u, j)  # , j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
        print()
    print(f"update[{k}] = {ok}")
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    print(f"update[{k}]")
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            print(u, j)  # , j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
        print()
    print(f"update[{k}] = {ok}")
    print()
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    print(f"update[{k}]: {update}")
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            print(u, j)  # , j in rule[u])
            ok = j in rules[u]
        if not ok:
            all_ok = False
        print()
    print(f"update[{k}] = {ok}")
    print()
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    print(f"update[{k}]: {update}")
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            ok = j in rules[u]
            print(f"{u}, {j}: ok = {ok}")
        if not ok:
            all_ok = False
        print()
    print(f"update[{k}] = {ok}")
    print()
print(f"all updates = {all_ok}")
rules
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    print(f"update[{k}]: {update}")
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            ok = j in rules[u]
            print(f"{j} in  rules[{u}] = {ok}")
        if not ok:
            all_ok = False
        print()
    print(f"update[{k}] = {ok}")
    print()
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[2:N]):
    ok = True
    print(f"update[{k}]: {update}")
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            ok = j in rules[u]
            print(f"{j} in  rules[{u}] = {ok}")
        if not ok:
            all_ok = False
    print(f"update[{k}] = {ok}")
    print()
print(f"all updates = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[0:N]):
    ok = True
    print(f"update[{k}]: {update}")
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            ok = j in rules[u]
            print(f"{j} in  rules[{u}] = {ok}")
        if not ok:
            all_ok = False
    print(f"update[{k}] = {ok}")
    print()
print(f"all_ok = {all_ok}")
k = 0
all_ok = True
N = len(updates)
for k, update in enumerate(updates[0:N]):
    ok = True
    print(f"update[{k}]: {update}")
    for i, u in enumerate(update):
        n = len(update)
        for j in update[i+1:n]:
            ok = j in rules[u]
            print(f"{j} in  rules[{u}] = {ok}")
        if not ok:
            all_ok = False
    print(f"update[{k}] = {ok}")
    print()
print(f"all_ok = {all_ok}")
