# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
filename = "story"
def read_file_content(filename):
    # [assignment] Add your code here
    with open("./story.txt", "r") as f:
        file_contents = f.read()
        return file_contents
# print(read_file_content(filename))

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    #print(split_text)
    count = {}
    words = text.split("count_words")
    for word in split_text:
        if word in count:
            count[word] += 1 
        else:
            count[word] = 1
    return(count) 

print(count_words())
    
  
