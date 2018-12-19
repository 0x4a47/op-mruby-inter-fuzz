# ???

The point of this is to reduce the corpus of an afl session to save time

Can be done at the very earliest once per Master fuzzer cycle

afl-cmin = remove cases that produce exact same code paths
afl-tmin = remove data in a test case that produces same code path (reduce file siize etc)

Reduce corpus of the current session queue (can be done on original test cases before you even start)
```
afl-cmin -i queue_all/ -o queue_cmin -- ~/parse
```

Parallel per-cases minimization (fast!!):
> see `afl-ptmin.sh`
