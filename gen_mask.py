import numpy as np
import os, glob
import cv2

mask_dir = 'output_mask'

label_path_list = glob.glob(os.path.join('FDDB-folds', '*ellipse*txt'))

for label_path in label_path_list:
    rf = open(label_path, 'r')
    # lines = f.readlines()

    img_path = rf.readline().strip()
    while img_path:
        print os.path.join(img_path, '*')
        img_path= glob.glob(img_path+'*')[0]
        face_num=int(rf.readline().strip())
        region_list = []
        for i in range(face_num):
            region_list.append(rf.readline().split())


        ### generate mask image
        # get img info
        img = cv2.imread(img_path,0)
        # h,w, = img.shape
        blank_img = np.zeros(img.shape)

        for region in region_list:
            region = [int(float(s)) for s in region]
            major_axis, minor_axis, angle, center_x, center_y, _ = region

            # draw ellipse on blank_img
            cv2.ellipse(blank_img,(center_x,center_y),(minor_axis,major_axis),angle,0,360, 255, -1)

        # wirte mask to file
        dir_name = os.path.join(mask_dir,os.path.dirname(img_path))
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        save_path = os.path.join(dir_name, os.path.basename(img_path))
        cv2.imwrite(save_path, blank_img)
        print save_path,'saved.'


        img_path = rf.readline().strip()
