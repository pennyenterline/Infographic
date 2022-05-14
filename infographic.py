###
### Author: Penny Enterline
### Course: CSc 110
### Description: asks the user for a text file input. counts all the words
###              finds the most used word of each section (capital, small, punctuated)
###              creates a bar graph graphic finding the total amounts of each
###              section.

from graphics import graphics

def reading_in(file_name):
    '''
    opens a file of words, reads all the words into a list, and closes the file
    file_name is a user input file
    '''
    openfile = open(file_name, 'r')
    words = []
    # Loops through the lines in the text file
    for line in openfile:
        line = line.strip('\n').split()
        # Loops through each word in the current line
        for word in line:
            words.append(word)
    openfile.close()
    return words

def dictionary_creation(words_list):
    '''
    counts the words in words_list and inputs it into a dictionary
    the key is the word and the element is the number of that word
    words_list is a list of all the words in the file
    '''
    words_dict = {}
    # Loops through each word in words_list
    for word in words_list:
        count = 0
        if word not in words_dict:
            # Loops through the words in words_list and count each time they appear
            for index in words_list:
                if index == word:
                    count += 1
            words_dict[word] = count
    return words_dict

def count_words(dictionary):
    '''
    assigns small, medium, and big words to their corresponding lists
    dictionary is made up of all the words and the number of words
    returns lists of small, medium, and big words
    small: 0-4 letters
    medium: 5-7 letters
    big: 8-any letters
    '''
    small_words, medium_words, big_words = [], [], []
    small_number, medium_number, big_number = 0, 0, 0
    for key in dictionary:
        if 0 <= len(key) <= 4:
            small_words.append(key)
            small_number += 1
        elif 5 <= len(key) <= 7:
            medium_words.append(key)
            medium_number += 1
        elif 8 <= len(key):
            big_words.append(key)
            big_number += 1
    return small_words, medium_words, big_words,

def total_count_words(dictionary):
    '''
    counts the number of small, medium, and big words
    small: 0-4 letters
    medium: 5-7 letters
    big: 8-any letters
    returns the number of these words
    '''
    small_number, medium_number, big_number = 0, 0, 0
    for key in dictionary:
        if 0 <= len(key) <= 4:
            small_number += 1
        elif 5 <= len(key) <= 7:
            medium_number += 1
        elif 8 <= len(key):
            big_number += 1
    return small_number, medium_number, big_number

def most_occurred(list, dictionary):
    '''
    finds the most used word in a list
    dictionary is made up of all the words and the number of words
    returns the most common word in the dictionary and the number of it
    '''
    current_word = list[0]
    for index in range(len(list)):
        if dictionary[list[index]] > dictionary[current_word]:
            current_word = list[index]
    most_common = dictionary[current_word]
    return current_word, most_common

def count_capital(dictionary):
    '''
    counts the amount of capital and non capital letters
    in the dictionary of words
    returns the amount of captial/noncapital
    '''
    capital = 0
    non_capital = 0
    # Loops through each word in words_dict
    for key in dictionary:
        if key[0] < 'a':
            capital += 1
        else:
            non_capital += 1
    return capital, non_capital

def count_punctuated(dictionary):
    '''
    counts the amount of punctuated and non punctuated letters
    in the dictionary of words
    returns the amount of punctuated/nonpunctuated
    '''
    punctuated = 0
    non_punctuated = 0
    # Loops through each word in words_dict
    for key in dictionary:
        if key[-1] == '.':
            punctuated += 1
        elif key[-1] == ',':
            punctuated += 1
        elif key[-1] == '?':
            punctuated += 1
        elif key[-1] == '!':
            punctuated += 1
        else:
            non_punctuated += 1
    return punctuated, non_punctuated

def bar_graph(gui, dictionary, capital_count, non_capital_count,
              punctuated_count, non_punctuated_count):
    '''
    creates the bar graphics out of the parameters
    dictionary: all the words and the number of words
    capital_count: numbers of capital words
    non_capital_count: numbers of non capital words
    punctuated_count: numbers of punctuated words
    non_punctuated_count: numbers of non punctuated words
    returns the bar heights to use for text later
    '''
    # calls total count words to count the number of small/med/big words
    small_word_count, medium_word_count, large_word_count = total_count_words(dictionary)
    total_number = len(dictionary)
    #creates color keys so lines arent as long
    light_blue = gui.get_color_string(124, 158, 183)
    pink = gui.get_color_string(255, 211, 215)
    #small bar
    gui.rectangle(-1, -1, 1000, 1000, gui.get_color_string(255, 243, 224))
    gui.rectangle(20, 200, 100, ((450 / total_number) * small_word_count), light_blue)
    small_bar_height = ((450 / total_number) * small_word_count)
    #medium bar
    gui.rectangle(20, 200 + small_bar_height, 100, ((450 / total_number) *
                                                    medium_word_count), pink)
    medium_bar_height = ((450 / total_number) * medium_word_count)
    #big bar
    gui.rectangle(20, 200 + small_bar_height + medium_bar_height, 100,
                  ((450 / total_number) * large_word_count), gui.get_color_string(124, 158, 183))
    #capital bar
    gui.rectangle(220, 200, 100, ((450 / total_number) * capital_count), light_blue)
    cap_bar_height = ((450 / total_number) * capital_count)
    gui.rectangle(220, 200 + cap_bar_height, 100, ((450 / total_number) *
                                                   non_capital_count), pink)
    #punctuated bar
    gui.rectangle(420, 200, 100, ((450 / total_number) * punctuated_count), light_blue)
    punctuated_bar_height = ((450 / total_number) * punctuated_count)
    gui.rectangle(420, 200 + punctuated_bar_height, 100, ((450 / total_number) *
                                                          non_punctuated_count), pink)
    return small_bar_height, medium_bar_height, cap_bar_height, punctuated_bar_height

def text_above_graph(gui, file_name, small_word, medium_word, big_word, small_count,
                     medium_count, big_count):
    '''
    creates the text above the graph, the title, and the stats
    small_word: most used small word
    medium_word: most used medium word
    big_word: most used big word
    small_count: number of most used small word
    medium_count: number of most used medium word
    big_count: number of most used big word
    '''
    light_blue = gui.get_color_string(124, 158, 183)
    lighter_blue = gui.get_color_string(197, 214, 219)
    gui.text(20, 170, 'Word Lengths', lighter_blue, 14)
    gui.text(220, 170, 'Cap/Non-Cap', lighter_blue, 14)
    gui.text(420, 170, 'Punct/Non-Punct', lighter_blue, 14)
    total_word_count = small_count + medium_count + big_count
    gui.text(20, 20, file_name, light_blue, 30)
    gui.text(20, 80, 'Total Unique Words: ' + str(total_word_count), lighter_blue, 15)
    gui.text(20, 120, 'Most used words (s/m/l): ', light_blue, 15)
    gui.text(250, 120, small_word + ' ' + '(' + str(small_count) + 'x)'
             + ' ' + medium_word + ' ' + '(' + str(medium_count) + 'x)'
             + ' ' + big_word + ' ' + '(' + str(big_count) + 'x)', light_blue, 15)\

def graph_dividers(gui, small_count, medium_count, big_count, capital_count,
                   non_capital_count, punctuated_count, non_punctuated_count,
                   small_bar_height, medium_bar_height, cap_bar_height, punctuated_bar_height):
    '''
    creates the text on the bars, labeling which part is which
    small_count: number of most used small word
    medium_count: number of most used medium word
    big_count: number of most used big word
    capital_count: number of capital words
    non_capital_count: number of non capital words
    punctuated_count: number of punctuated words
    non_punctuated_count: number of non punctuated words
    small_bar_height: height of small bar
    medium_bar_height: height of medium bar
    cap_bar_height: capital bar height
    punctuated_bar_height: punctuated bar height
    '''
    light_blue = gui.get_color_string(124, 158, 183)
    pink = gui.get_color_string(255, 211, 215)
    if small_count > 0:
        gui.text(20, 200, 'Small words', pink, 8)
    if medium_count > 0:
        gui.text(20, 200 + small_bar_height, 'Medium words', light_blue, 8)
    if big_count > 0:
        gui.text(20, 200 + small_bar_height + medium_bar_height, 'Large words', pink, 8)
    if capital_count > 0:
        gui.text(220, 200, 'Capitalized', pink, 8)
    if non_capital_count > 0:
        gui.text(220, 200 + cap_bar_height, 'Non Capitalized', light_blue, 8)
    if punctuated_count > 0:
        gui.text(420, 200, 'Punctuated', pink, 8)
    if non_punctuated_count > 0:
        gui.text(420, 200 + punctuated_bar_height, 'Non Punctuated', light_blue, 8)

def main():
    '''
    asks the user of file input
    call the functions to get values for variables
    creates the bar graph
    '''
    file_name = input('Enter file for infographic:\n')
    words_list = reading_in(file_name)
    dictionary = dictionary_creation(words_list)
    small_list, medium_list, big_list = count_words(dictionary)
    most_common_small, most_common_small_count = most_occurred(small_list, dictionary)
    most_common_medium, most_common_medium_count = most_occurred(medium_list, dictionary)
    most_common_big, most_common_big_count = most_occurred(big_list, dictionary)
    capital_count, non_capital_count = count_capital(dictionary)
    punctuated_count, non_punctuated_count = count_punctuated(dictionary)
    #creates canvas
    gui = graphics(650, 700, 'infographic')
    #calls the functions to create the bar graph
    while True:
        gui.clear()
        small_bar_height, medium_bar_height, cap_bar_height, punctuated_bar_height = \
            bar_graph(gui, dictionary, capital_count, non_capital_count,
                  punctuated_count, non_punctuated_count)
        text_above_graph(gui, file_name, most_common_small, most_common_medium,
                         most_common_big, most_common_small_count,
                         most_common_medium_count, most_common_big_count)
        graph_dividers(gui, most_common_small_count, most_common_medium_count, most_common_big_count,
                       capital_count,non_capital_count, punctuated_count, non_punctuated_count,
                       small_bar_height, medium_bar_height, cap_bar_height, punctuated_bar_height)
        gui.update_frame(30)

main()
