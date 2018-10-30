import os
import shutil


base_dir = "output_mask/"
new_img_dir = 'all-img'
new_mask_dir = 'all-mask'
for root, dirs, files in os.walk(base_dir, topdown=False):
    for name in files:
        img_path = os.path.join(root, name)
        old_img_name = img_path.replace(base_dir,'')
        img_name = old_img_name.replace('/','_')
        # print img_name
        new_mask_path = os.path.join(new_mask_dir,img_name)
        new_img_path = os.path.join(new_img_dir,img_name)
        shutil.copyfile(img_path,new_mask_path)
        print 'copy %s to %s' % (img_path,new_mask_path)
        

        shutil.copyfile(old_img_name,new_img_path)
        print 'copy %s to %s' % (old_img_name,new_img_path)




    # for name in dirs:
    #     print(os.path.join(root, name))