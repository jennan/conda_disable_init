import sys

from conda.plugins import hookimpl, CondaPreCommand


ERROR_MSG = """\
The 'conda init' command is disabled on this platform.
This command modifies ~/.bashrc in a way that triggers numerous issues.

Please use the following instead (once per session):

  source $(conda info --base)/etc/profile.d/conda.sh

Check the documentation to know more about how to use Conda on the HPC:

https://docs.nesi.org.nz/Scientific_Computing/Supported_Applications/Miniconda3/
"""


@hookimpl
def conda_pre_commands():
    def no_conda_init(command):
        sys.exit(ERROR_MSG)

    yield CondaPreCommand(
        name="pre-init-command", 
        action=no_conda_init,
        run_for={"init"},
    )
