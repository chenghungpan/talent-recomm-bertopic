# Introduction

This Talent Recommendation System is based on BERTopic model (##### https://github.com/MaartenGr/BERTopic) and adapted to add new recommendation engine.  In total, there are about 220,000 talent experiences in the dataset (talents_total.csv) And another Talent Training System has pre-trained a model (talent_sage_model), and two artifacts (talent_sage_topics and talent_sage_probs.npy). All these three files have been encapuslated into model.tar.gz and can be downloaded from the attached Google Dirve link.

At last,the front end browser of this application was implemented by Streamlit,which will be pip installed from the Step 2 (pip_install.sh). After Step 2, all of the dependencies should be in place for you to run.  In order for the dependencies to work, please ONLY USE PYTHON 3.9. Don't use 3.10 plus, or 3.8 minus, it will cause some dependencies issues and the application might not be working. 


### Step 1: Download the model files and data files form the following link:

#####   	https://drive.google.com/file/d/1JBYpdrwmVK53J2vLT9wkX8tOqUlbNX_2/view?usp=sharing

	 	model.tar.gz (size: 2632606239)

        ----------------------------------------------------------
		After downloading the file, run the following:
		% tar xvfz model.tar.gz 
		
		It will extract the following four files:

       	1) 	talent_sage_model		(pre-trained model)
		2)	talent_sage_probs.npy		(pre-trained similarity scores)
		3)	talent_sage_topics 		(pre-trained job titles)
		4) 	talents_total.csv   		(input data file) 

### Step 2: pip install the dependencies:

    % source ./pip_install.sh 

### Step 3: run the app 

   %  source ./run_main.sh


Final folder snapshot:

		pip_install.sh		(pip-install script)

 		run_main.sh		(run-main-program script)

 		talent_sage_model

 		talent_sage_probs.npy

 		talent_sage_topics

 		talents_total.csv

 		streamlit_load_model.py

 		topic_0.csv    (temperary file)
 		
		README        

## Examples
#### http://localhost:8501

![GitHub Logo](/images/Sample1.png)
![GitHub Logo](/images/Sample2.png)

# talent-recomm-bertopic
