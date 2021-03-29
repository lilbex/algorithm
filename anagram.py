def anagram(s1,s2):
#remove spaces and lowecase letters
    s1 =  s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    #return boolean for sorted match.
    if sorted(s1) == sorted(s2):
        return True
	
print(anagram('dog', 'god'))

def anagrams(s1,s2):
#remove spaces and lowecase letters
    s1 =  s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    #check if same number of letters
    if len(s1) != len(s2):
    	return False

    #count frequncy of each letter
    count = []

    for letter in s1: # for every letter in first string
        if letter in count: # if letter is already in my dictionary, then
            count[letter] += 1 # add 1 to that letter key
        else:
        	count[letter] = 1

        	# do reverse for second string
    for letter in s2:
    	if letter in count:
    		count[letter] -= 1
    	else:
    	    count[letter] = 1

    for k in count:
    	if count[k] != 0:
    		return False
    return True

print(anagrams('sus', 'god'))