# Facial Landmark Detection 

pip install -r requirements.txt

You also need shape detector, you can download it by 
```
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
```
# Usage
 ```
 python get_frames.py -i data/videos/example1.avi -f 1
 python facial_landmark_detection.py --shape-predictor shape_predictor_68_face_landmarks.dat --image data/images/example1
```
### Results
![Alt](results/result_m.png "Title")


### Reference
[One Millisecond Face Alignment with an Ensemble of Regression Trees, Kazemi and Sullivan (2014).](https://pdfs.semanticscholar.org/d78b/6a5b0dcaa81b1faea5fb0000045a62513567.pdf)


Credits: My Guru: Adrian Rosebrock 
