# Python-GIL-sample-codes
In this repository, Python codes are commited to compare execution time of thread-safety and free-thread.You can run and check the thread-safety and free-thread by the following commands.

- thread-safety
```
Python313/python.exe -c "import sys; print(sys._is_gil_enabled())"
True
```

- free-threaded
```
Python313/python3.13t.exe -c "import sys; print(sys._is_gil_enabled())"
False
```

## verification-examples
To simplify the command, export the following environment variables.
```
ve=verification-examples
```

### constraints-of-multithreading
```
Python313/python.exe $ve/constraints-of-multithreading/multi-threading.py
Multithreading Time: 3.702821731567383
```

```
Python313/python.exe $ve/constraints-of-multithreading/single-loop.py
Single-Loop Time: 3.7697293758392334
```
### enabled-gil-vs-disabled-gil

#### bubble-sort
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/bubble-sort/bubble-sort.py
Time: 6.924190282821655
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/bubble-sort/bubble-sort.py
Time: 4.428438425064087
```

#### bucket-sort
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/bucket-sort/bucket-sort.py
Time: 1.498405933380127
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/bucket-sort/bucket-sort.py
Time: 4.404151916503906
```

#### count-primes
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/count-primes/count-primes.py
Total Primes: 148933
Time: 2.0423481464385986
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/count-primes/count-primes.py
Total Primes: 148933
Time: 4.089309453964233
```

#### count-sort
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/count-sort/count-sort.py
Time: 12.022782564163208
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/count-sort/count-sort.py
Time: 9.198519945144653
```

#### fibonacci
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/fibonacci/fibonacci.py
Results: [9227465, 9227465, 9227465, 9227465]
Time: 22.125888347625732
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/fibonacci/fibonacci.py
Results: [9227465, 9227465, 9227465, 9227465]
Time: 6.238377332687378
```
#### fractal-generation
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/fractal-generation/fractal-generation.py
Time: 3.7402381896972656
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/fractal-generation/fractal-generation.py
Time: 4.890458106994629
```

#### matrix-calculation
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/matrix-calculation/matrix-calculation.py
Time: 3.2965750694274902
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/matrix-calculation/matrix-calculation.py
Time: 2.022977828979492
```

#### merge-sort
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/merge-sort/merge-sort.py
Time: 4.573821067810059
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/merge-sort/merge-sort.py
Time: 3.1484169960021973
```

#### prime-factors
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/prime-factors/prime-factors.py
Time: 3.378253936767578
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/prime-factors/prime-factors.py
Time: 6.371432542800903
```

#### quick-sort
```
Python313/python3.13t.exe $ve/enabled-gil-vs-disabled-gil/quick-sort/quick-sort.py
Time: 3.2474205493927
```

```
Python313/python.exe $ve/enabled-gil-vs-disabled-gil/quick-sort/quick-sort.py
Time: 2.9268484115600586
```

### leveraging-asynchronous-processing
```
Python313/python3.13t.exe $ve/leveraging-asynchronous-processing/asyncronous.py
Hello, Bob!
Hello, Alice!
Hello, Charlie!
Asyncronous Time: 3.0167410373687744 seconds
```

```
Python313/python.exe $ve/leveraging-asynchronous-processing/single-loop.py 
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Single-Loop Time: 6.003013849258423
```


### potential-race-conditions
```
Python313/python3.13t.exe $ve/potential-race-conditions/potential-race-conditions.py
Expected: 50000
Result: 25224
```

```
Python313/python.exe $ve/potential-race-conditions/potential-race-conditions.py
Expected: 50000
Result: 50000
```

### utilizing-multiprocessing

```
Python313/python.exe $ve/utilizing-multiprocessing/multi-processing.py 
Multiprocessing Time: 3.031339406967163
```

```
Python313/python.exe $ve/utilizing-multiprocessing/single-loop.py
Single-Loop Time: 3.8130526542663574
```
