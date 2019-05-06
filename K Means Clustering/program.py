#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:50:15 2019

@author: kushaldeb
"""
#Importing all the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5, 5)
plt.style.use('ggplot')

#Randomly initializing 1000 points each for x and y
x = []
y = []
x = np.random.uniform(1, 500, size=1000)
y = np.random.uniform(1, 500, size=1000)

#Combining x and y to create coordinate points
coordinates  = np.array(list(zip(x,y)))

#Randomly selecting number of centroids between 2 and 10
k = np.random.randint(2, 10)

#Function to calculate the distance between the points and the centroids
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

#Randomly selecting the coordinates of the centroids
centroid_x = np.random.uniform(0, np.max(coordinates)-20, size=k)
centroid_y = np.random.uniform(0, np.max(coordinates)-20, size=k)
centroid = np.array(list(zip(centroid_x, centroid_y)))

#Plotting the initial graph
plt.scatter(x, y, c='black', s=5)
plt.scatter(centroid_x, centroid_y, marker='+', s=100, c='r')

#Initializing centroid_old. It will store the old value of centroid
#after each iteration
centroid_old = np.shape(centroid.shape)
#Initializing clusters for each of the coordinates
clusters = np.zeros(len(coordinates))
#Error to check if the old centroid are same or not
error = dist(centroid, centroid_old, None)

#This loop will continue until the centroid does not changes
while error != 0:
    for i in range(len(coordinates)):
        #Calculates the distance of ith coordinate with each of the centroids
        distances = dist(coordinates[i], centroid)
        #Selects the centroid with the least distance to that ith coordinate
        #Assigns the sequence number of that centroid to the cluster
        cluster = np.argmin(distances)
        #Saves the cluster number for each ith coordinate
        clusters[i] = cluster
    #centroid_old takes the value of the previous centroid
    centroid_old = centroid
    
    #runs through the sequence number of each centroid
    for i in range(k):
        #points contains all the coordinates for the ith cluster
        points = [coordinates[j] for j in range(len(coordinates)) if clusters[j] == i]
        #new centroid is calculated using the mean of those points
        centroid[i] = np.mean(points, axis=0)
    #error is calculated between the old and new centroids
    error = dist(centroid, centroid_old, None)
    #this process is carried out until there is no change in the centroid.

#color scheme for different clusters.
#contains 10 colors for a maximum of 10 different clusters.
colors = ['#96ff00','#fffb00', '#f20993', '#92574a', '#00fffd', '#126362', '#4f5a71', '#e718e4', '#0052ff', '#f92e03']
#Plotting different clusters with their color schemes
fig, ax = plt.subplots()
for i in range(k):
        points = np.array([coordinates[j] for j in range(len(coordinates)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=5, c=colors[i])
ax.scatter(centroid[:, 0], centroid[:, 1], marker='+', s=100, c='r')
