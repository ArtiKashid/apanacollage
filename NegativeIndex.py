################################################################################
''' Python has a special feature like a negative index in Arrays and Lists.
 Positive index reads the elements from the starting of an array or list but
  in the negative index, Python reads elements from the end of an array or list.'''
##what will be the output of the given program( names[-1] gets
# Explaination:->the last item on the list which is 'Daman'.
# Then you get the last letter of that name 'Daman'[-1] which is 'n'
################################################################################

names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-1])
print(names[-1][-2])
print(names[0][0])
print(names[0][1])
print(names[1][0])