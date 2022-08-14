# Copyright Kopinjol Baishya
# contact: kopinjol@gmail.com

import string
import sys
import random
import numpy as np


class texts:
    def __init__(self, tfile):
        self.tfile = tfile

    def tread(self):
        fh = open(self.tfile, "r")
        l = fh.readlines()
        print(l)
        fh.close()
        print("3rd Line := \n")
        print(l[1])
        lwords = []
        for line in l:
            #print((line.split(' ')).strip())
            print('\n ')
            lwords.append(line.split(' '))

        print(lwords)
        words = []
        for i in range(0,len(lwords)):
        #for i in range(0, )
            #print(lwords[0][2])
            for j in range(0,len(lwords[i])):
                words.append((lwords[i][j]).lower())

        print("List of words :=")
        #print(words)
        self.mat_word = np.array(words)
        print("word array := ")
        #print(mat_word)
        for i in range(0, len(self.mat_word)):
            tmp = self.mat_word[i].strip()
            self.mat_word[i] = tmp

        print(self.mat_word)

        return(self.mat_word)

    # A simple generator.
    def count(self, list):
        #print("counting from 0 to {}".format(len(list)))
        print("len(list) = {}".format(len(list)))
        n = 0
        while(n < len(list)):
            yield n
            n += 1
            #print("i = {}".format(n))
        return



    def t_tok(self, mat_word):
        #pass
        regular_list = list(mat_word)
        tokenized_list = []
        tokenized_list.append(regular_list[0])
        for i in self.count(tokenized_list):
            #print("i = {}".format(i))
            for j in range(0, len(regular_list)):
                if tokenized_list[i] != regular_list[j]:
                    tokenized_list.append(regular_list[j])
                else:
                    pass

        print("Printing Tokenized list.")
        print(tokenized_list)

        for i in self.count(tokenized_list):
            pass




    #def main():
    #    b = tokenite.texts(sys.argv[1])
    #    W = b.tread()
    #    T = b.t_tok()
    #    #print(T)

    #if __name__=='__main__':
    #    main()
