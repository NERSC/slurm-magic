
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

First, things to do:

* Strategy (or no implementation) for interactive Slurm commands.
* The "mode" thing needs to be renamed.
* Logical approach to srun (auto-wrap in salloc?).
* Implement and document how to get help.

### %sacct

Display accounting data for all jobs and job steps in the Slurm job accounting log or Slurm database.
Is modal.

### %sacctmgr

View and modify Slurm account information.
Is modal.

### %salloc

Obtain a Slurm job allocation (a set of nodes), execute a command, and then release the allocation when the command is finished.

### %sattach (TBC)

Attach to a Slurm job step.

### %%sbatch

Submit a batch script to Slurm.

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

### %sbcast (TBC)

Transmit a file to the nodes allocated to a Slurm job.

### %scancel

Used to signal jobs or job steps that are under the control of Slurm.

### %scontrol

Used view and modify Slurm configuration and state.

### %sdiag

Scheduling diagnostic tool for Slurm.
Is modal.

### %sinfo

View information about Slurm nodes and partitions.
Is modal.

### %smap (TBC)

Graphically view information about Slurm jobs, partitions, and set configurations parameters.

### %sprio

View the factors that comprise a job's scheduling priority.
Is modal.

### %squeue

View information about jobs located in the Slurm scheduling queue.
Is modal.

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

### %sreport (TBC)

Generate reports from the slurm accounting data.

### %srun

Run parallel jobs.

### %sshare

Tool for listing the shares of associations to a cluster.
Is modal.

### %sstat (TBC)

Display various status information of a running job/step.

### %strigger (TBC)

Used set, get or clear Slurm trigger information.

### %sview (TBC)

Graphical user interface to view and modify Slurm state.

What Our Users Say
------------------

    I'll never have to leave a notebook again
    that's like the ultimate dream
