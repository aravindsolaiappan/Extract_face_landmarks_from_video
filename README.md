# Extract_Face_Landmarks_From_Video

pip install -r requirements.txt

You also need shape detector, you can download it by 
```
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
Download shape_predictor_68_face_landmarks.dat directly from the internet
```
# Usage
 ```
 python get_frames.py -i data/videos/example1.avi -f 1
 python facial_landmark_detection.py --shape-predictor shape_predictor_68_face_landmarks.dat --image data/images/example1
```
### Results
results/result_m.png "Title"
