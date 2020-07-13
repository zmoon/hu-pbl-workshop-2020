# hu-pbl-workshop-2020
Some of my stuff for the HU PBL Workshop

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zmoon92/hu-pbl-workshop-2020/master) (repo root)

## Repo info

* Jupyter NB extensions are enabled in `binder/postBuild` per [this binder example](https://mybinder.readthedocs.io/en/latest/sample_repos.html#enabling-jupyter-extensions-with-post-build-commands)
  - `widgetsnbextension` is installed when `ipywidgets` is installed via `conda`
  - `RISE` [doesn't have to be manually enabled](https://rise.readthedocs.io/en/stable/installation.html)
  - installing Jupyter NB extensions from conda-forge, the first line in the example [is not needed](https://github.com/ipython-contrib/jupyter_contrib_nbextensions#conda)
  - `toc2` is part of the "contrib" package, so `--py` not needed

* To create the environment locally, install the [Conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) in [`binder/environment.yml`](binder/environment.yml)
  ```
  conda env create -f environment.yml
  ```

  To run the notebooks, additionally install Jupyter Notebook with 
  ```
  conda install -c conda-forge notebook
  ```
  
  Or, run with another `jupyter` via `nb_conda_kernels` (note: no need to explicitly install `ipykernel` since it is a dependency of `ipywidgets` and will already have been installed).

* I am trying out [nbdime's Git integration](https://nbdime.readthedocs.io/en/latest/vcs.html#git-integration), for more informative diffs.
  - This requires that nbdime's tools are installed and available on your PATH for `git` to use. 
