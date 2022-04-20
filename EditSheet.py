import os


class AddToSheet:
    def __init__(self, file_path):
        self.FilePath = file_path

    def add_degree(self, student_id, degree):
        file_path = self.FilePath
        student_information_file = open(file_path, 'r')
        modified_data_list = []
        for line in student_information_file:
            split_line = line.split(',')
            if split_line[0] == student_id:
                new_line = line[:-1] + ',' + degree  # delete the last two character '\n' && add degree
                new_line = new_line + '\n'
                modified_data_list.append(new_line)
            else:
                modified_data_list.append(line)
        split_path = self.FilePath.split('/')
        split_path[len(split_path) - 1] = 'temp.csv'
        new_path = '/'
        for wordIndex in range(1, len(split_path)):
            new_path = new_path + split_path[wordIndex] + '/'
        new_path = new_path[:-1]
        temp_file = open(new_path, 'w')
        for record in modified_data_list:
            temp_file.write(record)
        os.remove(self.FilePath)
        os.rename(new_path, self.FilePath)
