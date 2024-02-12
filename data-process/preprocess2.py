import os
import numpy as np
import csv

def read_file(file_path,encoding='latin-1'):
    with open(file_path, 'r',encoding=encoding) as file:
        content = file.read()
    return content

def process_content(content, num_joints):
     lines = content.strip().split('\n')
     data_arrays = []
     for line in lines:
        if line[0].isdigit() or line[0] == '-':
            try:
                values = [float(val) for val in line.split(',') if val.strip()]
                data_arrays.append(np.array(values).reshape(num_joints,3))
            except ValueError as e:
                print (f'Error processing line:{line}.{e}')
     return data_arrays

def process_folder(folder_path, num_joints):
    data_arrays_list = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        content = read_file(file_path)
        data_arrays = process_content(content, num_joints)
        data_arrays_list.append(data_arrays)

    return data_arrays_list

def create_3d_array(data_arrays_list):
    num_files = len(data_arrays_list)
    num_joints = len(data_arrays_list[0][0])

    # Find the maximum number of frames among all files
    max_frames = max(len(data_arrays) for data_arrays in data_arrays_list)

    # Initialize a 3D array with zeros
    data_3d = np.zeros((num_files, max_frames, num_joints * 3))

    # Fill the array with data
    for i, data_arrays in enumerate(data_arrays_list):
        num_frames = len(data_arrays)
        
        for j in range(num_frames):
            data_3d[i, j, :] = data_arrays[j].flatten()

    return data_3d

# Example usage
correct_folder_path = 'Correct_postures'
incorrect_folder_path = 'incorrect_postures'

num_joints = 25  # Replace with the actual number of joints in your data
correct_data_arrays = process_folder(correct_folder_path, num_joints)
incorrect_data_arrays = process_folder(incorrect_folder_path, num_joints)

# Create 3D arrays
correct_data_3d = create_3d_array(correct_data_arrays)
incorrect_data_3d = create_3d_array(incorrect_data_arrays)
print((correct_data_3d[5].shape))
print(incorrect_data_3d[5].shape)
#Save to files
np.save('correct_data_3d.npy', correct_data_3d)
np.save('incorrect_data_3d.npy', incorrect_data_3d)