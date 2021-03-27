# Judge

This is a test generator for https://quera.ir/.  
Run main.py for generating testcases  
currently Judge only supports python3 and c++.  
currently, only works in linux

# config
```python
NAME = "problem"
SOL = ["sol.cpp", "sol.py"]
VAL = ["val.py"]
GEN = ["gen.cpp"]
CONF = [
    (0, 5, GEN[0], VAL[0], 10, 20),
    (1, 5, GEN[0], VAL[0], 10, 20),
]
SUBTASKS = [40, 60]
```

# NAME
name of the folder to store tests

# SOL
solutions  
first solution generate output and if other solutions
exists, checks their output.

# VAL
list of validators. (could be empty if you don't' need validator)

# GEN
list of test generators

# CONF
CONF contains pack of testcases.  
each pack is tuple of (subtask_number(zero based), number of test, generator, validator (could be None), *args to pass to generator)

# SUBTASKS
score of each subtask
