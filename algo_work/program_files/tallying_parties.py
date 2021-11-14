"""This is the file for where all code relating to the tallying up of parties shall go"""
def tally(mwcs):
    List_of_lists = [item for t in mwcs for item in t]
    print(List_of_lists)
    for i in range(len(List_of_lists)):
            count = List_of_lists.count(List_of_lists[i])
            print(List_of_lists[i], count)

# TODO - Find a way to store previously tallied parties so as to not end up with duplicate counts.

tally([[('B', 5), ('C', 3), ('D', 4), ('E', 3)], [('D', 4), ('E', 3), ('F', 8)]])