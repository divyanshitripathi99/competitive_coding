def shortestDistance(self, s, word1, word2):
    if word1 == word2:
	    return 0
	words = list(s)
	min_dist = len(words)+1
	for index in range(len(words)):
	    if (words[index] == word1):
	        for search in range(len(words)):
	            if (words[search] == word2):
	                 dist = abs(search - index) 
	            if(dist < min_dist):
                    min_dist = dist
    return(min_dist)
