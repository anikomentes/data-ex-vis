# Assignment: Image exploration

### Choose one of  (1A or 1B) and (2A or 2B)

## Create virtual environment with `uv`
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
python -m ipykernel install --user --name=dataexp_image_exploration --display-name "Python (dataexp_image_exploration)"
```
After running the above command, you should see the new kernel option "Python (dataexp_image_exploration)" when you create a new notebook in Jupyter Notebook/Lab. You can select this kernel to use the virtual environment for your image exploration tasks.
You might have to reload the page first to see the new kernel option.

## Create `conda` environment for the notebooks

```bash
conda env create -f environment.yml -n datavis_imageexp
```
Refreshing the notebooks page should be enough to see the new kernel option "Python (dataexp_image_exploration)". You can select this kernel to use the conda environment for your image exploration tasks.

If you use the environment in the terminal you will need to activate it first:
```bash
. /opt/conda/bin/activate
conda activate datavis_imageexp
```

If the above installation method doesn't work:
```bash
. /opt/conda/bin/activate
conda create -n datavis_imageexp python==3.12
conda activate datavis_imageexp 
conda install --yes --file requirements.txt
```
