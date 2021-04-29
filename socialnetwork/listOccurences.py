def listOccurences(item, names):
    # item is the list that you want to check, eg. ['cat','fish']
    # names contain the list of list you have.
    set_of_items = set(item) # set(['cat','fish'])
    count = 0
    for value in names:
        if set_of_items & set(value) == set_of_items:
            count+=1
    return count

