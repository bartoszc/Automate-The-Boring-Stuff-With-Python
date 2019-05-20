def print_table(tab):
    for j in range(len(tab[0])):
        for i in range(len(tab)):
            m = max([len(s) for s in tab[i]])
            print(tab[i][j].rjust(m), end=' ')
        print('')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
