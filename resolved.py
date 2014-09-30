#!/usr/bin/env python
# -*- coding: latin-1 -*-
__author__ = 'ctraistaru'


import random


NEWSPAPER = \
"""Officers received a call from a concerned passer-by who reported seeing
a dog left on the back seat of car parked on Church Lane in Mansfield.
The police officers smashed a window in the Mercedes and discovered
it was, in fact, a toy dog. The toy's owner, Gordon Williams, 80, said
police had done the right thing. I know Little Willy is quite realistic
and if they weren't sure about it, they did a good thing as we don't want
any more dogs dying in the heat of a car, said Mr Williams."""

LETTER = \
"""I have your dog. Bring one cheese cake and one purple rubber ball
and meet me at midnight at the gate of the cemetery if you want to see
him again."""


letters_dict = {}
ransom_letter_index_list = []


def create_letters_dict():
    letter_index = 0
    """Read every letter from the newspaper and give an index for every
    letter, then creating a dict with the letter as the key and for the
    value a list with all the occurrences from newspaper (index of every)"""
    for letter in NEWSPAPER.lower():
        for key in letters_dict:
            if key is letter:
                letters_dict[key].append(letter_index)
                continue
        letters_dict.setdefault(letter, [])
        letters_dict[letter].append(letter_index)
        letter_index += 1
    return letters_dict


def main():
    """Reading the ransom letter and selecting the needed letters for it, from
    the dict with all the occurrences we pick a letter then randomly select one
    of the occurrence, then remove the occurrence from the letter list of
    occurences"""
    create_letters_dict()
    for letter in LETTER.lower():
        for key in letters_dict.keys():
            if key is letter:
                index_used = random.choice(letters_dict[key])
                letters_dict[key].remove(index_used)
                ransom_letter_index_list.append(index_used)

    print ransom_letter_index_list
    print ""
    check_result()


def check_result():
    create_letters_dict()
    for index in ransom_letter_index_list:
        for key in letters_dict:
            if index in letters_dict[key]:
                print key,


if __name__ == '__main__':
    main()