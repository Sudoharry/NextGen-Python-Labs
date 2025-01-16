## Install this command to create a virtual environment for pip installation

sudo apt instal python3.12-venv


## Create a virtual environment

python3 -m venv myenv


## Now, we need to activate the myenv

source myenv/bin/activate

## Install the required libraries using the python pip installer package tool

pip install nltk

- This python libraries is essential for basic fundamental libraries for NLP in python. This is natural language toolkit


## Install the textblog

pip install textblob

- This is used for sentimental analysis which used nltk


## Install the newspaper3k

pip install newspaper3k

- This is essential library we are going to use, to get the newspaper articles into our script for sentimental analysis

