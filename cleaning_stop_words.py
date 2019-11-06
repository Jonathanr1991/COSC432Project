stop_words = ["the", "system", "shall", "product", "an", "a", "from", "to", "of", "in", "and", "for","or", "if", "be", "all","\"the", "notice", "implements", "have", "implement" ]

filepath1="training.txt"
filepath2="testing.txt"
filepath3="validate.txt"
training = open("training_clean.txt", "w")

text_file = open(filepath1, "r")

for text in text_file: 
    #removes unneeded text fron each line
    final_text=""
    text=text[text.find(":")+2:]
    text=text.lower()
    final_text=text[:text.find(",")-1]
    text=text[text.find(":")+2:]
    final_text+="- "+text[:text.find("\"")]

    #removed stop words from strings , modeled afer code from 
    # https://stackoverflow.com/questions/25346058/removing-list-of-words-from-a-string/25346119
    querywords = final_text.split()
    resultwords  = [word for word in querywords if word not in stop_words]
    result = ' '.join(resultwords)
    print(result)
    training.write(result+"\n")