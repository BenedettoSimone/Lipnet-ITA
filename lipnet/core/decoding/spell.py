import re
import string

from collections import Counter


# Source: https://github.com/commonsense/metanl/blob/master/metanl/token_utils.py
def untokenize(words: list) -> str:
	"""
	Untokenizing a text undoes the tokenizing operation, restoring
	punctuation and spaces to the places that people expect them to be.
	Ideally, `untokenize(tokenize(text))` should be identical to `text`,
	except for line breaks.
	"""
	text = ' '.join(words)

	step1 = text.replace("`` ", '"').replace(" ''", '"').replace('. . .',  '...')
	step2 = step1.replace(" ( ", " (").replace(" ) ", ") ")
	step3 = re.sub(r' ([.,:;?!%]+)([ \'"`])', r"\1\2", step2)
	step4 = re.sub(r' ([.,:;?!%]+)$', r"\1", step3)
	step5 = step4.replace(" '", "'").replace(" n't", "n't").replace("can not", "cannot")
	step6 = step5.replace(" ` ", " '")

	return step6.strip()


# Source: https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
def tokenize(text: str) -> list:
	return re.findall(r"\w+|[^\w\s]", text, re.UNICODE)


# Source: http://norvig.com/spell-correct.html
class Spell(object):

	def __init__(self, path: str):
		with open(path,'r',encoding='utf-8-sig') as f:
			word = f.read()
		print('word',self.words(word))
		self.dictionary = Counter(list(string.punctuation) + self.words(word) )
		print('dic: ',self.dictionary)

	@staticmethod
	def words(text: str) -> list:
		return text.split('\n')
		# return re.findall(r'\w+', text.lower())


	def p(self, word: str, n=None) -> float:
		"""Probability of `word`."""
		if n is None:
				n = sum(self.dictionary.values())
		return self.dictionary[word] / n


	def correction(self, word: list):
		"""Most probable spelling correction for word."""
		return max(self.candidates(word), key=self.p)


	def candidates(self, word):
		"""Generate possible spelling corrections for word."""
		# return self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word]
		return self.known([word]) or [word]


	def known(self, words) -> set:
		"""The subset of `words` that appear in the dictionary of WORDS."""
		return set(w for w in words if w in self.dictionary)


	@staticmethod
	def edits1(word: str) -> set:
		"""All edits that are one edit away from `word`."""
		letters    = 'abcdefghijklmnopqrstuvwxyz'
		letters    = 'ิื์ใ็้เ่๋า๊ีัํำไุูึะโ'
		for i in range(ord('ก'),ord('ฮ')):
			letters += chr(i)
		
		splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
		deletes    = [L + R[1:] for L, R in splits if R]
		transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
		replaces   = [L + c + R[1:] for L, R in splits if R for c in letters]
		inserts    = [L + c + R for L, R in splits for c in letters]
		return set(deletes + transposes + replaces + inserts)


	def edits2(self, word):
		"""All edits that are two edits away from `word`."""
		return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))


	# Correct words
	def corrections(self, words: list) -> list:
		return [self.correction(word) for word in words]


	# Correct sentence
	def sentence(self, sentence: str) -> str:
		print('sen',sentence)
		# an = untokenize(self.corrections(tokenize(sentence)))
		an = ''.join(self.corrections(tokenize(sentence)))
		print('an',an)
		return an 