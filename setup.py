from distutils.core import setup

README = open('README.md').read()

setup(
        author="R. C. Thomas",
        author_email="rcthomas@lbl.gov",
        description="IPython magic for SLURM.",
        long_description=README,
        name="slurm-magic",
        py_modules=["slurm_magic"],
        requires=["ipython"],
        url="NA",
        version="0.0.3"
)
