# No `conda init` command

This [Conda plugin](https://conda.io/projects/conda/en/latest/dev-guide/plugins/index.html) is meant to disable the `conda init` command, preventing users on an HPC system to insert an shell snippet that will conflict with the module system.


## Installation

From your base environment:

```
pip install git+https://github.com/jennan/conda_disable_init
```


## References

- https://conda.io/projects/conda/en/latest/dev-guide/plugins/index.html
- https://github.com/conda/conda-plugin-template/blob/main/tutorials/subcommands/python/README.md


