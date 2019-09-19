'''
Task # 5
'''

def get_snail_days(h, a, b):
    if b >= a:
        return 0
    elif h == a:
        return 1
    v_days = 0
    v_distance = 0
    while (v_distance < h):
        v_days += 1
        v_distance = v_distance + a - b
    return v_days

print get_snail_days(10, 3, 2)
print get_snail_days(10, 3, 1)
print get_snail_days(10, 6, 1)
print get_snail_days(10, 10, 1)
print get_snail_days(10, 1, 3)