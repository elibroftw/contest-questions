t = int(input())

# how this passes the second test set: storing calculations so that
# you don't have to do them again but can rather call a dict/map (memoize)
for case in range(t):
    n, m, q  = [int(x) for x in input().split()]
    torn_out_set = set()
    reader_dict = {}  # important for passing the second test set
    for page in input().split():
        page = int(page)
        torn_out_set.add(page - 1)
    pages_read = 0
    for reader in input().split():
        reader = int(reader)
        if reader not in reader_dict:
            reader_read = 0
            for page_read in range(reader - 1, n, reader):
                if page_read not in torn_out_set:
                    reader_read += 1
            reader_dict[reader] = reader_read
        pages_read += reader_dict[reader]
    print('Case #', case + 1, ': ', pages_read, sep='')
            