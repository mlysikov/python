'''
Task # 2. Option 1
'''

def get_vowels_list(p_text):
    v_list = []
    v_vowels = "aeiouAEIOU"
    for i in p_text:
        for j in v_vowels:
            if i == j:
                v_list.append(i)
    return v_list

print get_vowels_list('This is a test')
print get_vowels_list('THIS IS A TEST')
print get_vowels_list('THIS is A TeST')