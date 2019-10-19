# does not work for second test set

t = int(input())
for case in range(t):
    n, m, q  = [int(x) for x in input().split()]
    torn_out = [int(x) for x in input().split()]
    readers =  [int(x) for x in input().split()]
    
    torn_out_set = set()
    for page in torn_out:
        torn_out_set.add(page - 1)
        # torn_out_dict[page - 1] = -1
    pages_read = 0
    for reader in readers:
        for page_read in range(reader - 1, n, reader):
            if page_read not in torn_out_set:
                pages_read += 1
    print('Case #', case + 1, ': ', pages_read, sep='')
            