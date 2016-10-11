
from __future__ import print_function

import inspect
import io
from subprocess import (Popen, PIPE)
import sys

import pandas

from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic,
        line_cell_magic)
from IPython.core.magic_arguments import (argument, magic_arguments,
        parse_argstring)


def modal(func):
    def wrapped_func(obj, line):
        result = func(obj, line)
        if obj._display == "pandas":
            return pandas.read_table(io.StringIO(result), sep='\s+',
                    error_bad_lines=False)
        else:
            return result
    wrapped_func.__doc__ = func.__doc__
    return wrapped_func


@magics_class
class SlurmMagics(Magics):

    def __init__(self, shell=None, **kwargs):
        super(SlurmMagics, self).__init__(shell, **kwargs)
        self._display = "pandas"

    @line_magic
    def slurm(self, line):
        chunks = line.lower().split()
        variable, arguments = chunks[ 0 ], chunks[ 1 : ]
        if variable == "display" :
            return self._configure_display(arguments)

    def _configure_display(self, arguments):
        if arguments:
            mode = arguments[0]
            if mode not in [ "pandas", "raw" ] :
                raise ValueError("Unknown Slurm magics display mode", mode)
            self._display = mode
        return self._display

    @modal
    @line_magic
    def sacct(self, line):
        """Display accounting data for all jobs and job steps in the Slurm job
        accounting log or Slurm database."""
        return self._execute(line)

    @modal
    @line_magic
    def sacctmgr(self, line):
        """View and modify Slurm account information."""
        return self._execute(line)

    @line_magic
    def salloc(self, line):
        """Obtain a Slurm job allocation (a set of nodes), execute a command,
        and then release the allocation when the command is finished."""
        return self._execute(line)

    @line_magic
    def sattach(self, line):
        """Attach to a Slurm job step."""
        pass

    @line_cell_magic
    def sbatch(self, line, cell):
        """Submit a batch script to Slurm."""
        # FIXME Document further.
        return self._execute(line, input=cell.encode(encoding='UTF-8'))

    @line_magic
    def sbcast(self, line):
        """Transmit a file to the nodes allocated to a Slurm job."""
        pass

    @line_magic
    def scancel(self, line):
        """Used to signal jobs or job steps that are under the control of
        Slurm."""
        return self._execute(line)

    @line_magic
    def scontrol(self, line):
        """Used view and modify Slurm configuration and state."""
        return self._execute(line)

    @modal
    @line_magic
    def sdiag(self, line):
        """Scheduling diagnostic tool for Slurm."""
        return self._execute(line)

    @modal
    @line_magic
    def sinfo(self, line):
        """View information about Slurm nodes and partitions."""
        return self._execute(line)

    @line_magic
    def smap(self, line):
        """Graphically view information about Slurm jobs, partitions, and set
        configurations parameters."""
        pass

    @modal
    @line_magic
    def sprio(self, line):
        """View the factors that comprise a job's scheduling priority."""
        return self._execute(line)

    @modal
    @line_magic
    def squeue(self, line):
        """View information about jobs located in the Slurm scheduling
        queue."""
        return self._execute(line)

    @line_magic
    def sreport(self, line):
        """Generate reports from the slurm accounting data."""
        pass

    @line_magic
    def srun(self, line):
        """Run parallel jobs."""
        pass

    @modal
    @line_magic
    def sshare(self, line):
        """Tool for listing the shares of associations to a cluster."""
        return self._execute(line)

    @line_magic
    def sstat(self, line):
        """Display various status information of a running job/step."""
        pass

    @line_magic
    def strigger(self, line):
        """Used set, get or clear Slurm trigger information."""
        pass

    @line_magic
    def sview(self, line):
        """Graphical user interface to view and modify Slurm state."""
        pass

    def _execute(self, line, input=None, stderr=False):
        name = inspect.stack()[1][3]
        process = Popen([name] + line.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate(input)
        if stderr:
            return stdout.decode("utf-8"), stderr.decode("utf-8")
        else:
            return stdout.decode("utf-8")


def load_ipython_extension(ip):
    """Load extension in IPython."""
    slurm_magic = SlurmMagics(ip)
    ip.register_magics(slurm_magic)
