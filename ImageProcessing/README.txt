READ ME 

** IDEALLY we would have something that does step 2 for us but I am too lazy to write it now in python. 

1- Draw Image 
	- make sure that the orientation of the path so that positive movement means upwards 
	- save image in your directory 

2- Binarize. 
	- run binary.m on this image so that it outputs a binary text file for python to read 

3- Run Python for Excel 
	- run it like this in your command line 
		python getcsv.py the_image_binary.txt some_number

	some_number : that reflects how accurate your drawing. If you have a lot of curves you want to it to be a small number like 4 or 5 or so. If its lines. It doesnt really matter. This number is called Neighbor_hood size. 

	- check the figure if its the right path. If it's not painting in certain places make the some_number bigger. If it's painting in places it shouldnt be make it smaller. If nothing works and you cant find a threshold, draw a more zoomed in and accurate version of the image. 


4 - find your csv file 
	- you'll find it in your directory with the same name as the image
	- the formate 

								**FORMAT ** 
		angle_to_next_node    distance_to_next_node   paint_stutus