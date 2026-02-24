# Interactive visualizations

## A)
Reproduce an interactive report from the https://atlo.team/ website 
Their most popular visualizations are most probably on the https://atlo.team/koronamonitor/ page.

### Choose 3 figures which don't have the same visualization type!

## B)

Choose one of the assignments and make it interactive!
Create **two** types of interactivity:
    * **static**: in which all the data is loaded and the user can interact with it, but no new data is loaded during the interaction, e.g. hovering over a point to see its name
    * **dynamic**: a server is running in the background and new data is loaded during the interaction, e.g. a dropdown menu to select a country and load its data 

## How to share your work?
### You can use any visualization package, but it has to be
  * open source
  * portable, e.g. viewed in a browser
  * extendible by others, i.e. someone take it and continue working on it

Some of the popular packages are:
  * [**bokeh**](https://docs.bokeh.org/en/latest/)
  * [**plotly**](https://plotly.com/python/)
  * [**R shiny**](https://shiny.rstudio.com/)
  * [**RMarkdown**](https://rmarkdown.rstudio.com/)
  * [**a Jupyter book**](https://executablebooks.org/en/latest/)
  * [**or something similar that can be shared and viewed in a browser**](https://observablehq.com/)

### If you create a notebook, then **convert it to html**

 ```
 jupyter-nbconvert --to html --execute --no-input worksheet-interactive.ipynb
 ```
