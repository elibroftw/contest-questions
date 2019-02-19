# Keep track of how many rows and columns still need to be merged.
# While there are at least two rows that need to be merged or two columns that need to be merged:
#     Grab the next smallest edge in the graph.
#     If this edge connects two columns which have not yet been merged:
#         Multiply the edge weight by the number of unmerged rows and merge the columns
#     Else, if this edge connects two rows which have not yet been merged:
#         Multiply the edge weight by the number of unmerged columns and merge the rows
# Return the sum of the multiplied edge weights