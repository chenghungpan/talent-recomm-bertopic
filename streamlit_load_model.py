#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
import streamlit as st
from bertopic import BERTopic
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

score_treshold = 0.45      # similarity score threshold , from 0 to 1(100% identical)

dataset = pd.read_csv("talents_total.csv")
df0 = pd.DataFrame(dataset)
df = df0[["id","titleInExperience"]]
print('talent quantity=',len(df))

talent_exp=[]
talent_key=[]
for k in range(94000):
    talent_id = list(df.values[k])[0]
    work_exp =  list(df.values[k])[1]
    # exclude nan for work_exp
    if isinstance(work_exp,str):
        work_exp_list = work_exp.split(',')
        for exp in work_exp_list:
            new_exp=exp.strip()
            if len(new_exp)>1 and new_exp.lower()!='other':
                if ('/' in new_exp):
                    nest_exp_list = new_exp.split('/')
                    for exp2 in nest_exp_list:
                        talent_exp.append(exp2)
                        talent_key.append(talent_id)
                else:
                    talent_exp.append(exp)
                    talent_key.append(talent_id)
docs=talent_exp
print('docs len=',len(docs))
##############################
# Train model 
#  - commented out here.  Because we will load the pre-trained model.
#-----------------------------
# model = BERTopic(language="english", calculate_probabilities="True")
# topics, probs = model.fit_transform(docs)

##############################
# Load model
#-----------------------------
model = BERTopic.load("talent_sage_model")

# load topics & probs
topics = []
with open("talent_sage_topics", "r") as f:
    for line in f:
        topics.append(int(line.strip()))

probs=np.load("talent_sage_probs.npy")
########################
print('loading is done...',len(topics),len(probs))
   
placeholder = st.empty()
keyword = placeholder.text_area("Type in keywords for talent search", height=20)
###############

print(len(topics), len(docs), len(probs))

df2 = pd.DataFrame({'topic': topics[0:84000], 'document': docs[0:84000]})
topic_0 = df2[df2.topic == 0]
print("======================================================================================")
print("\t  Scores             "," Talent ID","         Resume  Cotent")
print("======================================================================================")

# find the top 5 most relevant topics(clusters)
similar_topic, similarity=model.find_topics(keyword,top_n=5); 

# extract searc keyword embedding
keyword_embedding = model._extract_embeddings([keyword],method="word",verbose=False).flatten()

max_score=0
max_talent_id=0
data = pd.DataFrame({
    'talentId': [],
    'score': [],
    'talentExp':[]
})

new_talentId = []
new_score = []
new_talentExp = []

for k in range(len(similar_topic)):
    topic_0 = df2[df2.topic == similar_topic[k]]

    total=(len(topic_0))
    # print(">>>",k,": Size=", total,"** TS(Topic Similarity)=",similarity[k])


    #  sim_doc: List of job experenice for talents  
    #  num_doc: List of similarity (score) for talents
    #  seq_doc: List of the talent ID of each talent
    sim_doc=[]
    num_doc=np.array([])
    seq_doc=[]

    topic_0 = df2[df2.topic == similar_topic[k]]

    topic_0.to_csv("topic_0.csv")
    topic_0 = pd.read_csv("topic_0.csv")

    for j in range(total):
        talent_experience = topic_0.iloc[j,2]
        talent_embedding = model._extract_embeddings([talent_experience],method="word",verbose=False).flatten()
        sims = cosine_similarity(keyword_embedding.reshape(1,-1),[talent_embedding])
        num_doc=np.insert(num_doc,0,sims[0])
        sim_doc.insert(0,talent_experience)
        seq_doc.insert(0,topic_0.iloc[j,0])

    # Sorting by the similary (score) of num_doc list
    out_arr = np.argsort(-num_doc)
    display_length = min(len(out_arr),10)

    for i in range(display_length):
        talent_id_sq = seq_doc[out_arr[i]]
        if num_doc[out_arr[i]]> score_treshold:
            
            this_talent_key = talent_key[talent_id_sq]
            this_score = num_doc[out_arr[i]]
            this_talentExp = sim_doc[out_arr[i]]
            
            new_talentId.append(this_talent_key)
            new_score.append(this_score)
            new_talentExp.append(this_talentExp)
            print(i+1,"\t",this_score,"\t",talent_id_sq,"/",this_talent_key,"\t",this_talentExp)
            
    
        if num_doc[out_arr[i]] > max_score:
            max_talent_id = sim_doc[out_arr[i]]
            max_score = num_doc[out_arr[i]]
            max_talent_key = seq_doc[out_arr[i]]


result_line = str(keyword)+"\t"+str(max_score)+"\t"+ str(max_talent_id + "\n") 


new_data = pd.DataFrame({
    'talentId': new_talentId,
    'score': new_score,
    'talentExp' : new_talentExp
})
data = data.append(new_data, ignore_index=True)
data2 = data.sort_values(ascending=0, by='score')



#  Output the talent recommendation
info_title = 'Recommended Talents: '+ str(len(data2))
if keyword != []:
    st.info(info_title)
    st.table(data2)



