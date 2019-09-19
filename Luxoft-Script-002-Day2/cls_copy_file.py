import shutil

class cls_copy_file:
    def __init__(self, p_file_from, p_file_to):
        self.__v_file_from = p_file_from
        self.__v_file_to = p_file_to
    
    def copy_file(self):
        try:
            shutil.copy(self.__v_file_from, self.__v_file_to)
            print 'File was copied successfully'
        except IOError as err:
            print 'Can\'t copy the file. ' + err.strerror