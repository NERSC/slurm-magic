
[![Build Status](https://travis-ci.org/NERSC/slurm-magic.svg?branch=master)](https://travis-ci.org/NERSC/slurm-magic)

SLURM-MAGIC
===========

This package implements [magic commands](http://ipython.readthedocs.io/en/stable/interactive/magics.html) for interacting with the [SLURM](http://slurm.schedmd.com/) workload manager.
SLURM magic simply wraps command-line executables and the commands themselves should look like their command-line counterparts.
Commands are spawned via [`subprocess`](https://docs.python.org/library/subprocess.html) and output captured in the notebook after being decoded to UTF-8.
Whatever arguments are accepted by a SLURM command line executable are also accepted by the corresponding magic command.
Mostly you just type whatever you'd usually type at the command line just with a % in front.

Some commands are modal.
The `%squeue` magic command respects a "pandas" mode meaning that the result can be returned as a [Pandas](http://pandas.pydata.org/pandas-docs/stable/) dataframe.
This may not be the best way to handle this kind of functionality, and may change.
Suggestions on how to handle the output are welcome --- the raw responses are not easily readable in IPython notebooks.

SLURM Magic Commands
--------------------

### %squeue

This is a line magic command that runs squeue.  
To switch to "pandas" mode simply do:

    In [2]: %mode pandas
    Out[2]: 'pandas'

Now the output from %squeue will be a Pandas dataframe:

    In [3]: %squeue -u rthomas
    Out[3]: 
         JOBID     USER ACCOUNT NAME PARTITION    QOS  NODES TIME_LIMIT  TIME ST  \
    0  2764292  rthomas   mpccc   sh     debug  debug      1      10:00  0:11  R   
    
       PRIORITY          SUBMIT_TIME           START_TIME  
    0     69060  2016-07-21T21:12:34  2016-07-21T21:13:21 

### %%sbatch

This is a cell magic command that takes the contents of a cell and submits it to the batch queue.

    In [2]: %%sbatch -p debug -t 10 -N 1
    #!/bin/bash
    srun -n 32 hostname
    ...: 
    Out[2]: u'Submitted batch job 2754280\n'
    
    In [3]: !cat slurm-2754280.out
    nid00044
    nid00044
    ...

What Our Users Say
------------------

    I’ll never have to leave a notebook again
    that’s like the ultimate dream
