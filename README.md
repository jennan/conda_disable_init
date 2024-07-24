# No `conda init` command

This [Conda plugin](https://conda.io/projects/conda/en/latest/dev-guide/plugins/index.html) is meant to disable the `conda init` command, preventing users on an HPC system to insert an shell snippet that will conflict with the module system.


## Build

To test building this repository as a Conda package:

```
conda create -p venv_build -c conda-forge -y conda conda-build
git clone https://github.com/jennan/conda_disable_init.git
conda run -p ./venv_build --live-stream conda build ./conda_disable_init/recipe/ --croot ./build
```


## References

- https://conda.io/projects/conda/en/latest/dev-guide/plugins/index.html
- https://github.com/conda/conda-plugin-template/blob/main/tutorials/subcommands/python/README.md


