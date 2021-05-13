# cars_cluster.py

Imagine a scenario where there are N cars on an infinitely long single-lane road. The cars are placed along the road and then told to start driving indefinitely.
Each car is driving at a constant speed but cannot pass a slower car in front of it, so once a car reaches a slower car it will match that car's speed.

Define a car cluster as a group of cars that are stuck traveling at the speed set by the slowest car in the front of its pack. Depending on the ordering, there may be many clusters traveling on the road simultaneously.


Given the speeds of N cars, construct an algorithm that counts the number of clusters.
Cars to do not speed up they can only slow down when joining a cluster.
