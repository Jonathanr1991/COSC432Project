
filepath = "Consolidated_data.txt"

text = open(filepath, "r")
#creating a file where to place the training data 40%
training = open("training.txt", "w")
#creating a file where to place the validating data 20%
validate = open("validate.txt", "w")
#creating a file where to place the testing data 20%
testing = open("testing.txt", "w")

performance =[]
maintainability=[]
operational=[]
security=[]
usability=[]


#reads in lines and picks out nonfunctional requirements with the corresponding categories  
for x in text: 

    if ("performance" in x):
        performance.append(x)
    if ("maintainability" in x):
        maintainability.append(x)
    if ("operational" in x):
        operational.append(x)
    if ("security" in x):
        security.append(x)
    if ("usability" in x):
        usability.append(x)

count = 1

for y in performance:
    if count==1 or count==2:
        print(y)
        training.write(y)
        count= count+1
        print (count)
    elif count==3:
        validate.write(y)
        count =count+1
    else:
        testing.write(y)
        count=1

count = 1

for y in maintainability:
    if count==1 or count==2:
        print(y)
        training.write(y)
        count= count+1
        print (count)
    elif count==3:
        validate.write(y)
        count =count+1
    else:
        testing.write(y)
        count=1

count = 1

for y in operational:
    if count==1 or count==2:
        print(y)
        training.write(y)
        count= count+1
        print (count)
    elif count==3:
        validate.write(y)
        count =count+1
    else:
        testing.write(y)
        count=1

for y in security:
    if count==1 or count==2:
        print(y)
        training.write(y)
        count= count+1
        print (count)
    elif count==3:
        validate.write(y)
        count =count+1
    else:
        testing.write(y)
        count=1


for y in usability:
    if count==1 or count==2:
        print(y)
        training.write(y)
        count= count+1
        print (count)
    elif count==3:
        validate.write(y)
        count =count+1
    else:
        testing.write(y)
        count=1