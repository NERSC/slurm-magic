from distutils.core import setup

setup(
        author="R. C. Thomas",
        author_email="rcthomas@lbl.gov",
        description="IPython magic for SLURM.",
        name="slurm-magic",
        packages=["slurm_magic"],
        requires=[],  # "pyslurm (>=15.08.8)' ah GPL ?
        url="NA",
        version="0.0.1"
)
