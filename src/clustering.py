
from tokenize import group
from tensorflow.keras.preprocessing.image import load_img 
from tensorflow.keras.preprocessing.image import img_to_array 
from tensorflow.keras.applications.vgg16 import preprocess_input 
from tensorflow.keras.applications.vgg16 import VGG16 
from tensorflow.keras.models import Model
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

from utils import view_cluster

import os
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle


# Image location
path = r"../temp/"
os.chdir(path)

# Image filenames
persons = []

with os.scandir(path) as files:
    for file in files:
        if file.name.endswith('.jpg'):
          # Add only jpg images
            persons.append(file.name)
            
# Create model   
model = VGG16()
model = Model(inputs = model.inputs, outputs = model.layers[-2].output)

def extract_features(file, model):
    # Force resize to 224x224 array
    img = load_img(file, target_size=(224,224))
    img = np.array(img) 
    reshaped_img = img.reshape(1,224,224,3) 
    imgx = preprocess_input(reshaped_img)
    # Get feature vector
    features = model.predict(imgx, use_multiprocessing=True)
    return features
   
data = {}
p = r"./temp/"

# Loop through every image
for person in persons:
    # Extract feature and dict
    try:
        feat = extract_features(person,model)
        data[person] = feat
    except:
        with open(p,'wb') as file:
            pickle.dump(data,file)
          
 
# List of the filenames
filenames = np.array(list(data.keys()))

# List of just the features
feat = np.array(list(data.values()))
feat = feat.reshape(-1,4096)


# Reduce the dimensions of the feature vector
pca = PCA(n_components=100, random_state=22)
pca.fit(feat)
x = pca.transform(feat)

# Cluster feature vectors
kmeans = KMeans(n_clusters=2, random_state=22)
kmeans.fit(x)

# Holds the cluster id and the images { id: [images] }
groups = {}
for file, cluster in zip(filenames, kmeans.labels_):
    if cluster not in groups.keys():
        groups[cluster] = []
        groups[cluster].append(file)
    else:
        groups[cluster].append(file)

view_cluster(groups[0])
view_cluster(groups[1])


   
# # Want to see which value for k might be the best ?
# sse = []
# list_k = list(range(3, 50))

# for k in list_k:
#     km = KMeans(n_clusters=k, random_state=22)
#     km.fit(x)
#     sse.append(km.inertia_)

# # Plot sse against k
# plt.figure(figsize=(6, 6))
# plt.plot(list_k, sse)
# plt.xlabel(r'Number of clusters *k*')
# plt.ylabel('Sum of squared distance');
# plt.show()