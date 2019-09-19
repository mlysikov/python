import os

class cls_delete_file:
    def __init__(self, p_file_name):
        self.__v_file_name = p_file_name

    def delete_file(self):
        if os.path.isfile(self.__v_file_name):
            os.remove(self.__v_file_name)
            print 'File was deleted successfully'
        else:
            print 'Selected file does not exist' 