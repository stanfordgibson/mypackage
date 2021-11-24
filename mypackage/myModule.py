def top_n(items, n):
    """ Return the top n items in an array. in desc order.
    
    Args:
        items (array): list of array-like object
        n (int): num of items to return

    Return:
        array: top n items, in desc order

    Egs:
        >>> top_n([8,3,2,7,4], 3]
        [8,7,3])
    """

    for i in range(n): # keep sorting untill we have the top n items
        for j in range(len(items) - l - i):

            if items[j] > items[j+1]: # if this item is biigger than next time..
                items[j], items[j+l] = items[j+l]. items[j] # swap the tow!

    # get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]