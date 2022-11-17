Step 1: Download the model files and data files form the following link:
		link address: 

       		talent_sage_model		(pre-trained model)
		talent_sage_probs.npy		(pre-trained similarity scores)
		talent_sage_topics 		(pre-trained job titles)

		talents_total.csv   		(input data file) 

Step 2: pip install the dependencies:

    % source ./pip_install.sh 

Step 3: run the app 

   %  source ./run_main.sh


Final folder snapshot:

-rw-r--r--  1 owner  staff        1995 Nov 16 19:47 pip_install.sh
-rw-r--r--  1 owner  staff          49 Nov 16 19:48 run_main.sh
-rw-r--r--@ 1 owner  staff  1826945222 Nov 16 19:57 talent_sage_model
-rw-r--r--@ 1 owner  staff  1173199088 Nov 16 19:57 talent_sage_probs.npy
-rw-r--r--@ 1 owner  staff      301714 Nov 16 19:57 talent_sage_topics
-rw-r--r--@ 1 owner  staff   122486188 Nov 16 19:58 talents_total.csv
-rw-r--r--@ 1 owner  staff        5033 Nov 16 20:07 streamlit_load_model.py
-rw-r--r--  1 owner  staff         747 Nov 16 20:07 topic_0.csv    (temperary file)
-rw-r--r--  1 owner  staff         206 Nov 16 20:11 README        
# talent-recomm-bertopic
