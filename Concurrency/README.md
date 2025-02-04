## Concepts:
- __Sync__: Blocking operations.
- __Async__: Non blocking operations.
- __Concurrency__: Making progress together.
- __Parallelism__: Making progress in parallel.

__Async__ and __Parallelism__ are forms of __Concurrency__

## Make the right choice
```
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
       print("Use Threads")
else:
    print("Multi Processing")
```

__Threads__ is used for tasks involve blocking operations:
- Working with Blocking Libraries: requests, sqlite3, csv, pandas,...
- Input Handling
- GUI applications
