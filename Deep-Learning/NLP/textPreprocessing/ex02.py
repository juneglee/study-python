# 한국어 처리 

# 한국어 토큰화의 어려움
# 1) 한국어는 교착어이다.
# 2) 한국어는 띄어쓰기가 영어보다 잘 지켜지지 않는다.

# 단어 토큰화가 아니라 정확히는 형태소(morpheme) 단위로 형태소 토큰화(morpheme tokenization)를 수행하게 됨

from konlpy.tag import Okt  
okt=Okt()  
print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# ['열심히', '코딩', '한', '당신', ',', '연휴', '에는', '여행', '을', '가봐요']
print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))  
# [('열심히', 'Adverb'), ('코딩', 'Noun'), ('한', 'Josa'), ('당신', 'Noun'), (',', 'Punctuation'), ('연휴', 'Noun'), ('에는', 'Josa'), ('여행', 'Noun'), ('을', 'Josa'), ('가봐요', 'Verb')]
print(okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# ['코딩', '당신', '연휴', '여행']

# 1) morphs : 형태소 추출
# 2) pos : 품사 태깅(Part-of-speech tagging)
# 3) nouns : 명사 추출

from konlpy.tag import Kkma  
kkma=Kkma()  
print(kkma.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# ['열심히', '코딩', '하', 'ㄴ', '당신', ',', '연휴', '에', '는', '여행', '을', '가보', '아요']
print(kkma.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))  
# [('열심히', 'MAG'), ('코딩', 'NNG'), ('하', 'XSV'), ('ㄴ', 'ETD'), ('당신', 'NP'), (',', 'SP'), ('연휴', 'NNG'), ('에', 'JKM'), ('는', 'JX'), ('여행', 'NNG'), ('을', 'JKO'), ('가보', 'VV'), ('아요', 'EFN')] 
print(kkma.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요")) 
# ['코딩', '당신', '연휴', '여행']

# 앞서 사용한 Okt 형태소 분석기와 결과가 다른 것을 볼 수 있습니다. 
# 각 형태소 분석기는 성능과 결과가 다르게 나오기 때문에, 형태소 분석기가 가장 적절한지를 판단하고 사용하면 된다.
# ex) 속도를 중시한다면 메킵을 사용할 수 있다 
