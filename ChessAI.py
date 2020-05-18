from chess import*

initialReal = [['r','n','b','q','k','b','n','r'],['p','p','p','p','p','p','p','p'],['_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_'],['P','P','P','P','P','P','P','P'],['R','N','B','Q','K','B','N','R']]


print("which explore method do you want to use. input \'1\'' or \'2\'")
exploreMethod = int(input())


print('***********************************')
print('Running full game with user        ')
print('type *finish* to end the game')
print('***********************************')
runGameUser(initialReal,exploreMethod)
