from collections import defaultdict
t = int(input())

# how this passes the second test set: storing calculations so that
# you don't have to do them again but can rather call a dict/map (memoize)
# remember adding True is adding 1 and adding False is adding 0

for case in range(t):
    n, m, q  = [int(x) for x in input().split()]
    torn_out_set = set()
    reader_dict = defaultdict(int) # important for passing the second test set
    for page in input().split():
        page = int(page)
        torn_out_set.add(page - 1)
    pages_read = 0
    for reader in input().split():
        reader = int(reader)
        if reader not in reader_dict:
            for page_read in range(reader - 1, n, reader):
                reader_dict[reader] += page_read not in torn_out_set
        pages_read += reader_dict[reader]
    print('Case #', case + 1, ': ', pages_read, sep='')
            