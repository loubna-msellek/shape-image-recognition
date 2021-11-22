

# Shape recognition 

Shape recognition is a Python code for detecting the number of squares, circles, triangles in a image.

## Installation

You can use the following line to install required libraries
```bash
pip install -r requirements.txt 
```



## Visualize the whole process for an image

You can use the visualization tool with the following line:
```bash
python3 visualization.py -i path-image -u path-label
```


### Results

![alt text](https://github.com/loubna-msellek/shape-image-recognition/tree/main/resultats/visualization_tool.png?raw=true)









## Testing the algorithm on labeled images

You can test the algorithm with the following line:
```bash
python3 test.py -i path-image -u path-label
```

Example with an image: 

```bash
python3 test.py -i data\001A0C0001467D-001F411-001DB46-0014C95-001CF0D001F38500163CF.jpg -u labels\001A0C0001467D-001F411-001DB46-0014C95-001CF0D001F38500163CF.txt
```

### Results
It will print out the contours detected and the number of shapes detected compared to the ground truth.

```bash
The number of squares predicted is: 1 out of 1
The number of circles predicted is: 1 out of 1
The number of triangles predicted is: 
1 out of 1
```
The following image for visualisation is also returned: 

![alt text](https://github.com/loubna-msellek/shape-image-recognition/tree/main/resultats/evaluate_final_image.png?raw=true)



## Evaluate on new unlabeled data

You can test the algorithm with the following line:
```bash
python3 evaluation.py -i path-image 
```

Example with an image: 

```bash
python3 evaluation.py -i data\001A12D0013BEE-001770F-0019E0F-0014E02-0016A5B0019C4C001A2BF.jpg 

```

### Results
It will print out the contours detected and the number of shapes detected compared to the ground truth.

```bash
The number of squares predicted is: 2 
The number of circles predicted is: 2
The number of triangles predicted is: 3
```
The following image for visualisation is also returned: 

![alt text](https://github.com/loubna-msellek/shape-image-recognition/tree/main/resultats/test_final_image.png?raw=true)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
