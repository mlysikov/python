class cls_get_file_content:
    def __init__(self, p_file_name):
        self.__v_file_name = p_file_name

    def get_all_content(self):
        try: 
            self.__v_file = open(self.__v_file_name, 'r')
            print 'Contents of the file ' + self.__v_file_name + ':'
            print self.__v_file.read()
            self.__v_file.close()
        except IOError as err:
            print 'Can\'t read the file. ' + err.strerror

    def get_content_by_line(self, p_line_number):
        try: 
            self.__v_file = open(self.__v_file_name, 'r')
            self.__v_lines = self.__v_file.readlines()
            self.__v_line_text = self.__v_lines[p_line_number - 1]
            print 'The ' + str(p_line_number) + ' line contains:'
            print self.__v_lines[p_line_number - 1]
            self.__v_file.close()
        except IOError as err:
            print 'Can\'t read the file. ' + err.strerror
        except IndexError:
            print 'Selected line #' + str(p_line_number) + ' does not exist'