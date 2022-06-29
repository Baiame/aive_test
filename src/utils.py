import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import load_img


def view_cluster(cluster):
    """
    Function that lets you view a cluster (based on identifier)    
    """
    plt.clf()
    plt.figure(figsize = (25,25));
    # Only allow up to 30 images to be shown at a time
    if len(cluster) > 30:
        print(f"Clipping cluster size from {len(cluster)} to 30")
        cluster = cluster[:29]
    # Plot each image in the cluster
    for index, file in enumerate(cluster):
        plt.subplot(10,10,index+1);
        img = load_img(file)
        img = np.array(img)
        plt.imshow(img)
        plt.axis('off')
    plt.show()
        