a = []
lower = 0
upper = 0
offset = 0
step = 0

a[lower:upper], a[lower:upper:], a[lower::step] = 0
a[lower:: upper] = 0
a[lower + offset: upper + offset] = 0
a[lower + offset:upper + offset] = 0
a[lower + offset: upper + offset] = 0
