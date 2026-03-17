# 🛠 Fundamentals & Data Integrity

### Data Cleaning and Filtering

* Tidy Data: Understanding observations (rows) vs. variables (columns).
* Imputation: Strategies for handling missing values (Mean, Median, Mode, or KNN).
* Outlier Detection: Using Z-scores or Interquartile Range (IQR).
* Data Constraints: Validating types (strings vs. floats) and range checks.

### Reproducibility

* Version Control: Using Git/GitHub for tracking code changes.
* Environment Management: Using Docker, Conda, or requirements.txt.
* Literate Programming: Combining prose and code (Jupyter Notebooks, Quarto).
* Seed Setting: Ensuring stochastic processes (like random splits) are repeatable.


### Virtual Environment

There is an already installed uv environment for this topic.
In order to use it in Jupyter Notebook/Lab, you need to add it as a kernel. To do this, run the following command:
```# activate the environment
source /v/courses/2026-dataexplorationandvisualization2026.public/uv_envs/dataexp_nlp/bin/activate
# install the kernel
python -m ipykernel install --user --name=dataexp_cleanfilter --display-name "Python (dataexp_cleanfilter)"
```
After running the above command, you should see the new kernel option "Python (dataexp_cleanfilter)" when you create a new notebook in Jupyter Notebook/Lab. You can select this kernel to use the virtual environment for your image exploration tasks.
You might have to reload the page first to see the new kernel option.

# Create virtual environment with `uv`
Create an environment first:
```
uv venv
```
Then install the required packages using a 'requirements.txt' file:
```
uv pip install -r requirements.txt
``` 

You need to have the 'ipykernel' package installed, which is included in the 'requirements.txt' file. This package allows you to use the virtual environment as a kernel in Jupyter Notebook.
To add the virtual environment as a kernel in Jupyter Notebook/Lab, run the following command:
```
# activate the environment
source .venv/bin/activate
# install the kernel
python -m ipykernel install --user --name=dataexp_cleanfilter --display-name "Python (dataexp_cleanfilter)"
```
After running the above command, you should see the new kernel option "Python (dataexp_cleanfilter)" when you create a new notebook in Jupyter Notebook/Lab. You can select this kernel to use the virtual environment for your image exploration tasks.
You might have to reload the page first to see the new kernel option.

## Create conda environment for the notebooks

Normally we start with `conda init`, but in Kooplex's docker container it does not work. Instead 
```bash
. /opt/conda/bin/activate
conda create -n datavis_cleanfilter --yes --file requirements.txt
```

### Some links for further reading
* https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4 # Not there anymore
* https://towardsdatascience.com/?s=handle+missing+data

* https://pypi.org/project/jupyter-datatables/


