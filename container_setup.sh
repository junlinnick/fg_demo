:<<CHECKIN


CHECKIN

print_log(){
    ts=`data + "%F %X"`
    echo "$ts [INFO]              $@"
}

# 检查root用户执行

if  [ "$(id -u) "!= "0"]; then 
        echo "This script must be run as root " 1 >&2
        exit 1

fi

setup_path=/data/checkin/setup_files

# nginx_conf=/etc/ngix/ngix.nginx_conf
mkdir -p /etc/yum.repos.d.bak
mv /etc/yum.repos.d/*  /etc/yum.repos.d.bak
mv $setup_path/.repo  /etc/yum.repos.d
yum clean all
yum make cache
#install anaconda
bash ${setup_files}/Anaconda3-2021.05-Linux-x86_64.sh-b
echo "export PATH=/root/anaconda3/bin:$PATH" >> /root/.bashrc
source ~/.bashrc

conda create -n env_dlib python=3.8 -y 

conda activate env_dlib

conda install -c conda-forge dlib  -y

pip install cmake -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install face_recognition -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install jsonfield  -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install Pillow  -i https://pypi.tuna.tsinghua.edu.cn/simple


\cp  -f /etc/hosts.bak /etc/hosts
yum clean all
rm -rf /var/cache/yum/*
rm -rf  ~/.cache/pip
