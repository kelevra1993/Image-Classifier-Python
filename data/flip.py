import cv2

###########
#IMPORTANT#
###########
number_files=2400

#first thing we do is create a large list with all of the paths for the training files

filenames_plus=["./PLUSIEURS_VEHICULES/%08d.tiff"%(i) for i in range(1,(number_files+1))]


#We initialize a file counter to keep track of our process
file_counter_plus=0

for image_path_plus in filenames_plus:
    
    file_counter_plus=file_counter_plus+1
    if(file_counter_plus%1000==0):
        print("%d out of %d files were processed"%((number_files),file_counter_plus))
    #open the grayscale* image, and generate it's one-hot vector label
    image=cv2.imread(image_path_plus)
    image=cv2.flip(image,1)
    cv2.imwrite("./PLUSIEURS_VEHICULES/%08d.tiff"%(file_counter_plus+number_files),image)
    
#first thing we do is create a large list with all of the paths for the training files
filenames_ok=["./OK/%08d.tiff"%(i) for i in range(1,(number_files+1))]

#We initialize a file counter to keep track of our process
file_counter_ok=0

for image_path_ok in filenames_ok:
    
    file_counter_ok=file_counter_ok+1
    if(file_counter_ok%1000==0):
        print("%d out of %d files were processed"%((number_files),file_counter_plus))
    #open the grayscale* image, and generate it's one-hot vector label
    image=cv2.imread(image_path_ok)
    image=cv2.flip(image,1)
    cv2.imwrite("./OK/%08d.tiff"%(file_counter_ok+number_files),image)