'''
Task # 1. Option 2. Without a second nested loop
'''

def get_vowels_count(p_text):
    v_count = 0
    v_vowels = "aeiouAEIOU"
    for i in p_text:
        if i in v_vowels:
            v_count += 1
    return v_count

print get_vowels_count('This is a test')
print get_vowels_count('THIS IS A TEST')
print get_vowels_count('THIS is A TeST')