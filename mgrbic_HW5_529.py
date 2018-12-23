def lastfirst(firstLast):
    first_names = []
    last_names = []
    for item in firstLast:
        first, last = item.split(',')
        first_names.append(first)
        last_names.append(last)
    print([last_names] + [first_names])
#use the function in idle, lastfirst(["Last, First", "Last2, First2"])



