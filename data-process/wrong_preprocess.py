import os
import numpy as np

def read_file(file_path,encoding='latin-1'):
    with open(file_path,'r',encoding=encoding) as file:
        content = file.read()
    return content


def process_content(content,):
    lines = content.strip().split('\n')
    data_arrays = []
    for line in lines:
        if line[0].isdigit() or line[0] == '-':
            try:
                values = [float(val) for val in line.split(',') if val.strip()]
                data_arrays.append(np.array(values).reshape(25,3))
            except ValueError as e:
                print (f'Error processing line:{line}.{e}')
    return data_arrays

def process_folder(folder_path):
    data_arrays_list = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path,filename)
        content = read_file(file_path)
        data_arrays = process_content(content)
        data_arrays_list.extend(data_arrays)
    
    return data_arrays_list

incorrect_data_array = process_folder('incorrect_postures')
correct_data_array = process_folder('Correct_postures')
# Assuming correct_data_arrays and incorrect_data_arrays are your data arrays
correct_data_arrays = np.array(correct_data_array)
incorrect_data_arrays = np.array(incorrect_data_array)

# Save to files
# np.save('correct_data1.npy', correct_data_arrays)
# np.save('incorrect_data1.npy', incorrect_data_arrays)

print(incorrect_data_array[0].shape)
#print(len(correct_data_array))