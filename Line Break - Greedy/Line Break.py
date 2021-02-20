#!/usr/bin/env python
# coding: utf-8

# Line Break - Greedy
# Gourav Siddhad

#################################################################

def word_wrap(wordseq, linewidth):
    word, newseq = '', ''
    llen = 0

    for i, letter in enumerate(wordseq):
        if letter != ' ':
            word += letter
        else:
            if len(word) + llen <= linewidth:
                newseq += word + ' '
                llen += len(word) + 1
            else:
                newseq += '\n' + word + ' '
                llen = len(word) + 1
            word = ''

        if i == len(wordseq)-1 and letter != ' ':
            if len(word) + llen <= linewidth:
                newseq += word + ' '
                llen += len(word) + 1
            else:
                newseq += '\n' + word + ' '
                llen = len(word) + 1
            word = ''
    return newseq

#################################################################


# First Query
newseq = word_wrap('aaa bb cc ddddd', 6)
print(newseq, end='\n\n')

# Second Query
newseq = word_wrap('This is known as the word wrap problem', 10)
print(newseq, end='\n\n')

# Third Query
newseq = word_wrap('This is the solution to a problem', 12)
print(newseq, end='\n\n')

#################################################################

wordseq = input('Enter Word Sequence : ')
linewidth = int(input('Enter Line Width : '))
newseq = word_wrap(wordseq, linewidth)
print(newseq, end='\n\n')
