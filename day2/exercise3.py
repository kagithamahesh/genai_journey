import string

# // clean text
def getStringVal(msg):
    msg = msg.lower()
    msg = msg.translate(str.maketrans(" "," ",string.punctuation))

    return msg


print(getStringVal("hello's, world. enter  "))