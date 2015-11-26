import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

def print_sq_dict(dict):
    for j in dict:
        print(j, dict[j])

def cosine_similarity(vec1, vec2):
    numerator = 0
    local_vec2 = vec2[:]#copy so as to during remove-time does not alter origional vector

    #goes through every possible key in vec1 and vec2 and compares if they're the same
    for i in vec1:
        for j in range(len(local_vec2)):
            if i == local_vec2[j]:

                #sums their product if they are the same (as in a dot product?)
                numerator += vec1[i] * local_vec2[j]
                del local_vec2[j] #deletes so it is not checked again.
                break

    #divides by the norm of the other 2 before returning
    return numerator/(norm(vec1)*norm(vec2))


def build_semantic_descriptors(sentences):
    semantic_descriptors = {}

    #loops through every sentence
    for sentence in sentences:
        #casts to set to remove duplicates
        sentence_set = set(sentence)

        #check if word is already present in semantic_descriptors
        for word in sentence_set:
            if word not in semantic_descriptors:
                semantic_descriptors[word] = {}

            #if not in semantic_descriptors, calculate the new words to be associated with semantic_descriptors[j]
            #add in a new slot with value 1 if does not exist, else increment.
            for second_word in sentence_set:
                #makes sure the word does not appear in it's own semantic_descriptors
                if second_word == word:
                    continue
                if second_word not in semantic_descriptors[word]:
                    semantic_descriptors[word][second_word] = 1
                else:
                    semantic_descriptors[word][second_word] += 1

    return semantic_descriptors


def build_semantic_descriptors_from_files(filenames):
    file_text = ""
    text_list = []
    #loops through all the files and concatenates them together
    for files in filenames:
        file_text += open(files, "r", encoding="utf-8").read()
        file_text += " "

    #cleans up punctuation and capitalization, makes all sentence-ending-punctuation into "." to make for easy splitting
    file_text = file_text.lower().translate({ord(','):"", ord("-"):" ", ord(":"):" ", ord(";"):" ", ord('"'):" ", ord("'"):" ",ord('.'):".", ord('?'):".", ord('!'):"."})

    #splits the file_text into the list of lists needed by build_semantic_descriptors
    for lines in file_text.split("."):
        text_list.append(lines.split())

    return build_semantic_descriptors(text_list)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    result = -1
    result_similarity = -1

    #checks if the word being checked against is valid
    if word not in semantic_descriptors:
        return result

    #loops through every possible choice
    for choice in choices:
        #if choice doesn't exist, break to next choice option
        if choice not in semantic_descriptors:
            continue
        #calcualtes similarity of present choice, if exceeds the previous, replace result and result_similarity
        calculated_similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        if calculated_similarity > result_similarity:
            result = choice
            result_similarity = calculated_similarity

    return result
 #############################UNDERSTAND TEH FUCKING NULL CASE?!?!?!?! OF SIMILARITY_FN()##############################


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    #reads in all the questions from text and splits them into lists, one line (thus question) per list
    file_text = open(filename, "r", encoding="utf-8").read().split("/n")
    answers_correct = 0

    #checks if the question that most_similar_word returns is the same as the one specified, if so, increments correct_answers
    for question in file_text:
        if question[1] = most_similar_word(question[0], question[2:len(question), semantic_descriptors, similarity_fn]):
        answers_correct += 1

    #converts number of correct_answers into a percent of the total number of questions
    return answers_correct/len(file_text)*100

if __name__ == "__main__":
    d = {"potato":1, "hi":2}
    for j, k in d.items():
        print(j)
        print(k)

    d1 = {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}
    d2 = {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}
    print(cosine_similarity(d1,d2))

    sentences = [['i', 'am', 'a', 'sick', 'man'],
    ['i', 'am', 'a', 'spiteful', 'man'],
    ['i', 'am', 'an', 'unattractive', 'man'],
    ['i', 'believe', 'my', 'liver', 'is', 'diseased'],
    ['however', 'i', 'know', 'nothing', 'at', 'all', 'about', 'my', 'disease', 'and', 'do', 'not', 'know', 'for', 'certain', 'what', 'ails', 'me']]

    #print_sq_dict(build_semantic_descriptors(sentences))
    x = build_semantic_descriptors_from_files(["text.txt"])
    print(x == build_semantic_descriptors(sentences))
    print(build_semantic_descriptors_from_files(["text.txt"]))

    y = "hi"
    print(y)
    y = 5
    print(y)

    list = [1,2,3,4,5,6]
    for j in range(1):
        for i in list:
            print(i)
            list.remove(i)
    print(list)