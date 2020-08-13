def has_a(word_list): # define a function that takes in a list  
    a_list = []    # make an empty list

    for word in word_list:      # for each word in the inputted list
        if "a" in word.lower(): # if it has the letter a in it
            a_list.append(word) # add it to the a_list

    return a_list

def is_even(word_list):   # define a function that takes in a list
    even_list = []    # make an empty list

    for word in word_list:         # for each word in the list
        if len(word) % 2 == 0:     # if it has an even length
            even_list.append(word) # add it to the even_list

    return even_list