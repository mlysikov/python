'''
Task # 4
'''

def check_arith_geo(p_list):
    if len(p_list) < 2:
        return "Not enough elements"
    v_arith = p_list[1] - p_list[0]
    v_geo = p_list[1] / p_list[0]
    for i in range(2, len(p_list)):
        if p_list[i] - p_list[i - 1] == v_arith:
            v_result = "Arithmetic"
        elif p_list[i] / p_list[i-1] == v_geo:
            v_result = "Geometric"
        else:
            v_result = "Neither arithmetic, nor geometric"
            break
    return v_result

print check_arith_geo([1, 3, 5, 7])
print check_arith_geo([5, 15, 45])
print check_arith_geo([1, 10, 3])
print check_arith_geo([1])