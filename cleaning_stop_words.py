stop_words = ["the", "system", "shall", "product", "an", "a", "from", "to", "of", "in", "and", "must", "able","could","it","want",
"for","or", "if", "be", "all","\"the", "notice", "implements", "have", "implement" , "has", "this",
"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", 
"yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", 
"itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", 
"this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", 
"have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", 
"if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against",
 "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up",
  "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here",
   "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most",
    "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", 
    "very", "s", "t", "can", "will", "just", "don", "should", "now"]

filepath1="data_clean.txt"

training = open("data_clean_2.txt", "w")

text_file = open(filepath1, "r")


for text in text_file: 


    #removed stop words from strings , modeled afer code from 
    # https://stackoverflow.com/questions/25346058/removing-list-of-words-from-a-string/25346119
    querywords = text.split()
    resultwords  = [word for word in querywords if word not in stop_words]
    result = ' '.join(resultwords)
    print(result)
    training.write(result+"\n")

