user_input = input("문자열을 입력하세요: ")
# 문자열을 대시('-')로 분리하여 단어들을 리스트로 만듭니다.
words = user_input.split('-')
acronym_list = [word[0].upper() for word in words]


# 리스트의 각 요소를 합쳐서 새로운 문자열을 생성합니다.
acronym = ''.join(acronym_list)

print(words)
#%%
