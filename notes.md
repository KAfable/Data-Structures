# Data Structures

## Linked Lists

- Linked list nodes contain the value as well as a pointer to the next item
  [![Linked Lists](https://i.imgur.com/DlHeCzG.png)](https://www.youtube.com/watch?v=-Yn5DU0_-lw&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=6)
  [![Linked Lists](https://i.imgur.com/LK86MyA.png)](https://www.youtube.com/watch?v=-Yn5DU0_-lw&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=6)
-

## Least-Recently-Used Cache (LRU Cache)

### What Are Caches

- bits of storage that keep copies of data in fast but small storage
- primary storage that is relatively slow (like a hard drive)
- cache hit - when the data you want is in the cache
- cache miss - when you have to go to the primary storage to get the data

### LRU Cache

- limited in size compared to primary storage
- strategy to prioritzing items that is in the cache
- LRU discards the least-recently used item in the cache when it is full
- keeps the most-recently used item in the cache

### Building an LRU Cache

- needs a hash table to look up cache entries by key
  - has constant time when looking up items by key
- cache entries are in a doubly-linked list
  - has constant time when moving items around in it
  - this is good because you are going to be adding/deleting from it
- you can use a hash table
- Applications of LRU Caches
- How would you add functionality to the cache to remove entries that are older than a cutoff age?
  - traverse down the list until you hit a node that is older, remove all nodes after that
- How would you remove entries as above in O(1) time?
  - Initially you can search and remove all of the entries that are older than the cutoff O(n)
  - and then any new updates to the cache can remove the older ones
  - could you add another hash table entry that also keeps track of the oldest?

## Queues

- queues are good for serializing data from multiple sources
  - eg if a server is handling requests form multiple sources, it will put them in a queue
- they are not general-purpose versus arrays or linked lists

## Questions
