Enhancing the predictive power of Google Trends data through network analysis: An infodemiology study of COVID-19

## Execution
This respoitory contains 2 programs, a download worker and a aggregrator. 


### Download Worker
**Directory: `downloader`**

The download worker utilizes the Python library [pytrends](https://pypi.org/project/pytrends) to obtain relative search volume (RSV) data and [click](https://pypi.org/project/click) to accept user inputs.

To run, execute `python download.py`.


### Aggregrator
**Directory: `scripts`**

After the raw data is obtained, one can proceed to merge the RSV.

Each Jupyter notebook are prefixed with a number, and should be executed in ascending order to replicate the result. 


#### Graphics
Most of the illustrations published were created using [seaborn](https://seaborn.pydata.org/) or [matplotlib](https://matplotlib.org/).

The scripts can be found under `scripts/graphics` directory, and the output illustrations can be found under `graphs` directory.
