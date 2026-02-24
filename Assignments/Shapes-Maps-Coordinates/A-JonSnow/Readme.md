## Following Jon Snow and discover the poisoned wells

 * geopandas, shapely, folium
 
### Additional reading related to this epidemic
* "Loss in the Time of Cholera: Long-run Impact of a DiseaseEpidemic on the Urban Landscape" http://economics.mit.edu/files/10841/
* "Data. (re)Imagined." https://medium.com/matter-driven-narrative/data-re-imagined-8feb517faf06
* "Lesson on Infographics from John Snow (no, not that Jon Snow)" https://medium.com/@juniageisler/lesson-on-infographics-from-john-snow-no-not-that-jon-snow-4ae6672bb64
* "Looking Beyond the Pump Handle - 
What a Cholera Outbreak can Teach us about Homeland Security." https://medium.com/homeland-security/looking-beyond-the-pump-handle-dc56217f8e32

See an earlier solution of this assignment in the public directory Examples/Shapes-Maps-Coordinates!

# Shapes, Maps, and Coordinates

There is an already installed uv environment for this topic.
In order to use it in Jupyter Notebook/Lab, you need to add it as a kernel. To do this, run the following command:
```# activate the environment
source /v/courses/2026-dataexplorationandvisualization2026.public/uv_envs/dataexp_shapesmaps/bin/activate
# install the kernel
python -m ipykernel install --user --name=dataexp_shapesmaps --display-name "Python (dataexp_shapesmaps)"
```
After running the above command, you should see the new kernel option "Python (dataexp_shapesmaps)" when you create a new notebook in Jupyter Notebook/Lab. You can select this kernel to use the virtual environment for your image exploration tasks.
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
python -m ipykernel install --user --name=dataexp_networks --display-name "Python (dataexp_networks)"
```
After running the above command, you should see the new kernel option "Python (dataexp_networks)" when you create a new notebook in Jupyter Notebook/Lab. You can select this kernel to use the virtual environment for your image exploration tasks.
You might have to reload the page first to see the new kernel option.

## Create conda environment for the notebooks

Normally we start with `conda init`, but in Kooplex's docker container it does not work. Instead 
```bash
. /opt/conda/bin/activate
conda create -n datavis_shapesmaps --yes --file requirements.txt
```
