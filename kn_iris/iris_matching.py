import os
from kn_iris.feature_vec import *
import  pickle, numpy as np, re

import threading
try:
    import queue
    que=queue.Queue()
except ImportError:
    from multiprocessing import Queue 
    que=Queue()


from scipy.spatial import distance

try:
    import itertools.imap as map
except ImportError:
    pass

import operator



def iris_recg(test_db_model_path,image):

            data = pickle.loads(open(test_db_model_path, "rb").read())
            # print("[INFO] loading encodings...")
            process_this_frame = True
            iris_encodings = data["encodings"]
            names = data["names"]
            q = que
            iris_name = threading.Thread(target=match_thread(iris_encodings,names,image,q)).start()
            while not q.empty():
                return q.get()




def match_thread(iris_encodings,names,iris_image,q):
        iris_encodings_in_image = engroup(iris_image)
        if iris_encodings_in_image !="invalid image":
            match = find_match(iris_encodings, names, iris_encodings_in_image)
            q.put(match)
        else:
            q.put("unmatch")



def hamming_check_string(str1,str2):
        hamming_distance_value = 0
        hamming_distance_value=np.sum((np.array(map(int, str1))) != (np.array(map(int, str2))))
        return hamming_distance_value





def compare_iris_encodings(known_iris, iris_encodings_in_image,name):
    finalVal = 0
    hamming_distance_value=0
    hamming_distance=0
    finalVal2=0
    for iriss in known_iris:
        hgroup1, vgroup1 = iriss
        
        hgroup2, vgroup2 = iris_encodings_in_image

        hamming_distance_value = distance_loop1(hgroup1, hgroup2)
        hamming_distance_value += distance_loop2(vgroup1, vgroup2, hamming_distance_value)	  
        finalVal2=finalVal2+hamming_distance_value
    print("++++++++hamming_distance1+++++++++",name,finalVal2)
    return finalVal2



def valuation(hgroup1, hgroup2,vgroup1, vgroup2):
    distnc1=distance.cdist(hgroup1, hgroup2,'hamming') 
    distnc2=distance.cdist(vgroup1, vgroup2,'hamming')
    value1=np.average(distnc1)
    value2=np.average(distnc2)


def distance_loop(str1, str2):
    assert len(str1) == len(str2)
    ne = operator.ne
    return sum(imap(ne, str1, str2))

def distance_loop1(hgroup1, hgroup2):
    

    hamming_distance_value = 0
    for row in range(13):
        # hgroup1[row] is a list of 32 members
        for col in range(32):      
            hamming_distance_value += hamming_check_string(hgroup1[row][col],hgroup2[row][col])

    return hamming_distance_value

def distance_loop2(vgroup1, vgroup2, hamming_distance_value):
    for row in range(36):
        for col in range(9):

            hamming_distance_value += hamming_check_string(vgroup1[row][col],vgroup2[row][col])	
    return hamming_distance_value

def find_match(known_iris, names, iris_encodings_in_image):
        namevalue=""
        matchlist=[]
        for index,iriss in enumerate(known_iris):
            # print("hamming_dist_iriss",index,len(iriss))
            matches = compare_iris_encodings(iriss, iris_encodings_in_image,names[index])
            
            if matches !=0:
                matchlist.append(matches)
            else:
                matchlist.append(2000)    
        # print("totallist",matchlist,names,(matchlist.index(min(matchlist))),matchlist[(matchlist.index(min(matchlist)))])  
        if matchlist[(matchlist.index(min(matchlist)))]<4500:
            namevalue = names[(matchlist.index(min(matchlist)))] 
            # print("match",str(namevalue),matchlist[(matchlist.index(min(matchlist)))])
            return str(namevalue)
        else:
            return "unmatch"


