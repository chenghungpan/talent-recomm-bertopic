Step 1: Download the model files and data files form the following link:

    	https://drive.google.com/file/d/1JBYpdrwmVK53J2vLT9wkX8tOqUlbNX_2/view?usp=sharing

	 	model.tar.gz (size: 2632606239)

             ----------------------------------------------------------
		After downloading the file, run the following:
		% tar xvfz model.tar.gz 
		
		It will extract the following four files:

       		1) 	talent_sage_model		(pre-trained model)
		2)	talent_sage_probs.npy		(pre-trained similarity scores)
		3)	talent_sage_topics 		(pre-trained job titles)
		4) 	talents_total.csv   		(input data file) 

Step 2: pip install the dependencies:

    % source ./pip_install.sh 

Step 3: run the app 

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

# talent-recomm-bertopic
