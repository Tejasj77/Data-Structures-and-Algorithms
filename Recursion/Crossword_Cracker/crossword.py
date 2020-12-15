crossword = [['+','+','+','+','+','+','+','+','+','+'],
             ['+','-','-','-','-','-','-','+','+','+'],
             ['+','+','+','-','+','+','+','+','+','+'],
             ['+','+','+','-','+','+','+','+','+','+'],
             ['+','+','+','-','-','-','-','-','+','+'],
             ['+','+','+','+','+','+','-','+','+','+'],
             ['+','+','+','+','+','+','-','+','+','+'],
             ['+','+','+','+','+','+','-','+','+','+'],
             ['+','+','+','+','+','+','-','+','+','+'],
             ['+','+','+','+','+','+','+','+','+','+'],
             ]

words = ['POLAND','LHASA','SPAIN','INDIA']
def traverse(cross,word_list):
    fetched_word = []
    word,iteration = 0,0
    i,j = 0,0
    for i in range(len(cross)):
        for j in range(len(cross[i])):
            if cross[i][j] == '-':
                if word_list[word][iteration] in fetched_word:
                    pass
                else:
                    while iteration<=len(cross[word]):
                        cross[i][j] = word_list[word][iteration]
                        pass



