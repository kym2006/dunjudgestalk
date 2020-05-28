import p1
import p2
res = []
for x in p2.li:
    if x not in p1.li:
        res.append(x)

print(res)