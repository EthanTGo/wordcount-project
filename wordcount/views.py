from django.http import HttpResponse
from django.shortcuts import render
import operator
#request object



def home(request):
	return render(request,'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split() #convert string into a list of words #space is used to separate word

	word_dictionary = {}
	for word in wordlist:
		if word in word_dictionary:
			word_dictionary[word] += 1
			#increase
		else:
			#add to the dictionary
			word_dictionary[word] = 1

	sorted_words = sorted(word_dictionary.items(), key = operator.itemgetter(1), reverse = True)
	return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sorted_words':sorted_words})

def about(request):
	return render(request, 'about.html')