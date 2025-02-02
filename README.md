# Hiperparameter Tuning Techniques

\## Objective This project aims to compare different methods for
hiperparameter tuning for different models. Specifically, we will
compare the following methods: - Grid Search - Random Search - Bayesian
Optimization - Genetic Algorithm

For the following models: - Linear regression - Random Forest -
XGBoost - Neural network

## Environment

The project is developed in both Python and R. The R environment is
defined in the `renv.lock` file contained within `/code/r_code`. To
create the environment, run the following command:

``` bash
Rscript -e 'renv::restore()'
```

For Python, everything was developed in a conda environment. The
environment file is in the root of the repository. To create the
environment, run the following command:

``` bash
conda env create -f environment.yml
```

## Dataset

## Structure of the repository

The repository is structured as follows:

## Running the project

If you want to replicate the results of this project, you can run each
file separately. Each file contains the code to run the different
methods for hiperparameter tuning for each model.

## Results

If your objective is to read and learn more about hiperparemeter tuning
techniques and the results of this analysis, you can read my notes in
this github page:
<https://villafuertem.github.io/hiperparameter_tuning/>
