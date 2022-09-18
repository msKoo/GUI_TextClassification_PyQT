import re
from bs4 import BeautifulSoup
from konlpy.tag import Okt

def pre_html(raw_review):
  # 1. html 제거
  review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
  return (review_text)

def pre_reg(raw_review):
  # 2. 영문자가 아닌 문자는 공백으로 변환
  letters_only = re.sub('[^ㄱ-ㅎ|ㅏ-ㅣ|가-힣]', ' ', raw_review)
  return (letters_only)

def pre_stop(raw_review, stopwords):
  if len(stopwords) == 0:
    stopwords = ['이', '있', '하', '것', '들', '그', '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때',
                 '년', '가', '한', '지', '대하', '오', '말', '일', '그렇', '위하']

  # 3. 단어 분리
  words = raw_review.split()
  # 5. stopwords 제거
  meaningful_words = [w for w in words if not w in stopwords]
  return (' ').join(meaningful_words)

def pre_stem(raw_review):
  # 6. 어간 추출
  # meaningful_sentence = (' ').join(meaningful_words)
  stemming_word = [word[0] for word in Okt().pos(raw_review, stem=True) if word[1] not in ['Josa', 'Eomi', 'Punctuation']]
  return (' '.join(stemming_word))
