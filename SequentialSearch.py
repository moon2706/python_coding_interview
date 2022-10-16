def sequential_search(list_,n):
    for i in list_:
        if i==n:
            break
        return True

elements=range(0,21)
ss=sequential_search(elements,4)
print(ss)

'''The searching algorithms are the algorithms that are used to search a particular value 
in a data structure such as lists in Python. For example, imagine that you are trying to find a 
specific card from a deck of cards. You will go through each card in the deck one by one until you
 find the card you are looking for. Once you got the card you were looking for you will stop. 
 This is how the sequential search algorithm works. Here is how to implement it using Python:'''