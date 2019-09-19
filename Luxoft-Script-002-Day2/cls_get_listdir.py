import os

class cls_get_listdir:
    def __init__(self, p_dir_name):
        self.__v_dir_name = p_dir_name
            
    def get_listdir(self):
        if os.path.isdir(self.__v_dir_name):
            self.__v_dir_list = os.listdir(self.__v_dir_name)
            print 'Contents of the directory ' + self.__v_dir_name + ':'
            for f in self.__v_dir_list:
                print f      
        else:
            print 'Selected directory or path does not exist'        