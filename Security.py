map = input(">")
i = 0
x = []

while i < len(map):
    x.append(map[i])
    i += 1

money = '$'
thief = 'T'
guard = 'G'

m = 0
while m < len(map):
    if x[m] == money:
        money_index = m
        m = len(map)
    else:
        m =+ 1

t = 0
while t < len(map):
    if x[t] == thief:
        thief_index = t
        t = len(map)
    else:
        t =+ 1

g = 0
while g < len(map):
    if x[g] == guard:
        guard_index = g
        g = len(map)
    else:
        g =+ 1

if thief_index < guard_index and guard_index < money_index:
    a = 0

elif money_index < guard_index and guard_index < thief_index:
    a = 1

elif thief_index < money_index and money_index < guard_index:
    print("ALARM")

elif money_index < thief_index and thief_index < guard_index:
    print("ALARM")

elif guard_index < money_index and money_index < thief_index:
    print("ALARM")

elif guard_index < thief_index and thief_index < money_index:
    print("ALARM")
    