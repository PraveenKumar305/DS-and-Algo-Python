#Hash Tables are data structures which generally provide very fast(O(1)) lookups, insertions and deletions
#In Python, dictionaries are implemented as hash tables.

#The way hashing works is that there is a bucket containing slots to fill with elements.
#Like in arrays, elements are referenced by their integer indexes, in dictionaries, or hash tables,
#values are referenced by their keys, which can be of any data type.
#Now there are different kinds of hash functions (eg: MD5, SHA1, SHA256) which are used to convert the keys into hashes, which are unique for each key
#And the hashes are then mapped to some slot in the bucket. And the key and value pair get stored in the slot,
#or in some accompanying data structure within the slot (like, linked lists)

#In general, the lookup, insert and delete operations all are very fast, in the order of O(1)
#But in some cases, more than one keys can map to the same slot and that increases the time complexity by some margin,
#although not by a lot in most cases. This is known as a collision.