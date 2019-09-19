'''
Task # 1. Option 1
'''

def get_vowels_count(p_text):
    v_count = 0
    v_vowels = "aeiouAEIOU"
    for i in p_text:
        for j in v_vowels:
            if i == j:
                v_count += 1
    return v_count

print get_vowels_count('This is a test')
print get_vowels_count('THIS IS A TEST')
print get_vowels_count('THIS is A TeST')