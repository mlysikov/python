class cls_create_file:
    def __init__(self, p_file_name, p_text):
        self.__v_file_name = p_file_name
        self.__v_text = p_text
    
    def create_file(self):
        try:
            self.__v_file = open(self.__v_file_name, 'w')
            self.__v_file.write(self.__v_text)
            print 'File was created successfully'
        except IOError as err:
            print 'Can\'t create the file. ' + err.strerror