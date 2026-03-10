import os
def read_txt(file_path):
    with open(file_path,"r") as f:
        return f.read()
    
# if __name__=="__main__":
#     print(read_txt(file_path="job_description.txt"))