import os, shutil
name_path=r'C:\Users\kkkk\Desktop\name.txt'
all = []
with open(name_path,'r') as f:
    for line in f.readlines():
        curLine = line.strip().split("	")
#         print(curLine)
        all.append(curLine)
        
f.close()
select_name=[[curr[0],int(curr[1])] for curr in all if int(curr[1]) > 1]

for curr in select_name:
    print(curr)
    name=curr[0]
    path='H:/project/face_recognition_jl/KNOWN_FACES/'+name
    target_path='H:/project/face_recognition_jl/UNKNOWN_FACES/'
    file_path='H:/LWF_dataset/lfw/lfw/'+name+'/'+name
    konwn_file_path=file_path+'_0001.jpg'
    unknow_file_path_list=[file_path+'_000{}.jpg'.format(i) for i in range(2,curr[1]+1) if i < 10]
    print(unknow_file_path_list)
    if not os.path.exists(path):
      #如果不存在则创建目录
      #创建目录操作函数
        os.makedirs(path) 
        print(path+' 创建成功')
        shutil.copy(konwn_file_path,path)
    for tmp_path in unknow_file_path_list:
        shutil.copy(tmp_path,target_path)