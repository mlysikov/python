'''
Task # 2. Option 2
'''

def get_vowels_list(p_text):
    v_list = []
    v_vowels = "aeiouAEIOU"
    for i in p_text:
        if i in v_vowels:
            v_list.append(i)
    return v_list

print get_vowels_list('This is a test')
print get_vowels_list('THIS IS A TEST')
print get_vowels_list('THIS is A TeST')