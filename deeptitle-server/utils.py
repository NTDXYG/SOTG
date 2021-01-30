from nltk.corpus import stopwords
from nltk import word_tokenize

stop_words = set(stopwords.words('english'))

def sim_jaccard(s1, s2):
    """jaccard相似度"""
    s1, s2 = set(s1), set(s2)
    ret1 = s1.intersection(s2)  # 交集
    ret2 = s1.union(s2)  # 并集
    sim = 1.0 * len(ret1) / len(ret2)
    return sim

def get_score(sentence, title_list):
    result_list = []
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    for i, text in enumerate(title_list):
        score = sim_jaccard(filtered_sentence, text.split())
        result_list.append((score, text))
    result_list.sort(reverse=True)
    return result_list[:5]
