print 'What do you want to do?'
print '1 - Contents of the selected directory'
print '2 - Contents of the file'
print '3 - Copy file'
print '4 - Create file'
print '5 - Delete file'

v_to_do = raw_input('Enter choice:')

if v_to_do == '1':
    import cls_get_listdir
    v_dir = raw_input('Please input a directory name including a full path:')
    obj_dir = cls_get_listdir.cls_get_listdir(v_dir)
    obj_dir.get_listdir()
elif v_to_do == '2':
    import cls_get_file_content
    v_file_name = raw_input('Please input a file name that you want to read including a full path:')
    obj_file = cls_get_file_content.cls_get_file_content(v_file_name)
    obj_file.get_all_content()
elif v_to_do == '3':
    import cls_copy_file
    v_file_from = raw_input('Please input a file name that you want to copy including a full path:')
    v_file_to = raw_input('Please input a destination path:')
    obj_copy = cls_copy_file.cls_copy_file(v_file_from, v_file_to)
    obj_copy.copy_file()
elif v_to_do == '4':
    import cls_create_file
    v_file_name = raw_input('Please input a file name that you want to create including a full path:')
    v_text = raw_input('Please input a text:')
    obj_create = cls_create_file.cls_create_file(v_file_name, v_text)
    obj_create.create_file()
elif v_to_do == '5':
    import cls_delete_file
    v_file_name = raw_input('Please input a file name that you want to delete including a full path:')
    obj_delete = cls_delete_file.cls_delete_file(v_file_name)
    obj_delete.delete_file()
else:
    print 'The choice is out of range'