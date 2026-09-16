from pattern.web import URL, DOM, plaintext
import pprint

# ~ url = URL('http://www.reddit.com/top/',unicode=True)
# ~ dom = DOM(url.download(cached=False))
# ~ for e in dom('div.entry')[:3]: # Top 3 reddit entries.
	# ~ print (e)
	# ~ for a in e('a.title')[:1]: # First <a class="title">.
		# ~ print (repr(plaintext(a.content)))


from pattern.web import URL, plaintext
s = URL('https://www.uantwerpen.be/en/research-groups/clips/').download()
s = plaintext(s, keep={'h1':[], 'h2':[], 'strong':[], 'a':['href']})
print(s)
