
from __future__ import print_function

from io import StringIO
from os import getcwd
from os.path import basename
from subprocess import Popen, PIPE

import sys


from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)


def modal(func):
    def wrapped_func(obj, line):
        result = func(obj, line)
        if obj._mode == "pandas":
            import pandas
            return pandas.read_table(StringIO(result), sep='\s+')
        else:
            return result
    return wrapped_func


@magics_class
class SlurmMagics(Magics):

    def __init__(self, shell=None, **kwargs):
        super(SlurmMagics, self).__init__(shell, **kwargs)
        self._mode = None

    @line_magic
    def mode(self, line):
        cleaned = line.strip().lower()
        if cleaned:
            if cleaned == "pandas":
                self._mode = "pandas"
            elif cleaned == "none":
                self._mode = None
            else:
                raise ValueError("Unknown SLURM magics mode:", line)
        else:
            if not hasattr(self, "_mode"):
                self._mode = None
        return self._mode if self._mode else "no mode set"

    @modal
    @line_magic
    def squeue(self, line):
        return self._squeue(line)

    @cell_magic
    def sbatch(self, line, cell):
        with StringIO(cell) as stdin:
            return self._execute(["sbatch"] + line.split(), input=cell,
                                 stderr=True)

    def _squeue(self, line):
        return self._slurm_line_magic("squeue", line)

    def _slurm_line_magic(self, command, line):
        return self._execute([command] + line.split())

    def _slurm_cell_magic(self, command, line, cell):
        # doesn't do anything.
        return command, line, cell

    def _execute(self, args, input=None, stderr=False):
        process = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate(input)
        if stderr:
            return stdout.decode("utf-8"), stderr.decode("utf-8")
        else:
            return stdout.decode("utf-8")


def load_ipython_extension(ip):
    """Load extension in IPython."""
    slurm_magic = SlurmMagics(ip)
    ip.register_magics(slurm_magic)
