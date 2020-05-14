# import the necessary packages
from imutils import paths
import pickle
import os
from kn_iris.feature_vec import *





def iris_test_model(train_db_path,train_db_model_path):
    directory_list = list()
    for root, dirs, files in os.walk(
            train_db_path,
            topdown=False):
        for name in dirs:
            directory_list.append(os.path.join(root, name))

    print ("directory_list", directory_list)
    iris_names=[]
    iris_name_encodings=[]
    invalid_image=False
    for directory in directory_list:
        # grab the paths to the input images in our dataset
        paths_to_images = list(paths.list_files(os.path.join(directory)))
        # initialize the list of iris_name_encodings and iris_names
        iris_encodings = []
        name = directory.split(os.path.sep)[-1]
    
        print ("name",name)
        # Encode the images located in the folder to thier respective numpy arrays
        invalid_image=False
        for path_to_image in paths_to_images:
            print ("path_to_image",path_to_image)
            # image = scipy.misc.imread(path_to_image)
            iris_encodings_in_image = engroup(path_to_image)
            if iris_encodings_in_image=="invalid image":
                invalid_image=True
            # face_encodings_in_image = get_face_encodings(path_to_image)

            iris_encodings.append(iris_encodings_in_image)
        if invalid_image == True :    
            print("invalid_image",name)
            invalid_image=False
        else:
            iris_names.append(name)     
            iris_name_encodings.append(iris_encodings)




    print ("train_db_model_path",len(iris_names),len(iris_name_encodings))
    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": iris_name_encodings, "names": iris_names}
    f = open(train_db_model_path, "wb")
    f.write(pickle.dumps(data))
    f.close()
    print ("OK")
    return iris_names




















