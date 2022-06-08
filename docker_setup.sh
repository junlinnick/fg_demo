today=`data   "+%Y%m%d"`
author=jl
commet="构建基础镜像${today}"
host_setup_base_path=/data/checkin/base_images/
image_id=8652b9f0cb4c
version=v1

img_name=checkin_sys
image_tag=checkin_image_base_${today}_${version}
container_name=checkin_container_${today}_${version}

setup_files_path=$host_setup_base_path/setup_files_path
host_mapped_path=/data/checkin/mapped_data
container_base_path=/data/checkin

container_setup_path=$container_base_path/setup_files
container_mapped_path=$container_base_path/mapped

docker  run \
-v $host_mapped_path:$container_mapped_path  \
--network bridge -d \
--name $container_name \
--privileged=true \
$image_id /usr/sbin/init


#copy files to container
docker exec $container_name /bin/bash -c "mkdir -p  ${container_base_path"
docker cp $host_setup_base_path $container_name:$container_base_path


docker exec $container_name /bin/bash -c "sh $container_setup_path/container_setup.sh"
docker exec $container_name /bin/bash -c  "rm -r  $container_setup_path"

docker commit -m "$comment"  -a "author" $container_name $img_name:${image_tag}
##test#
 docker run -v /Users/mengzi/documents/project/face_recognition_jl/checkin:/data/checkin -d  -p  8080:8080 --name checkin_sys_test1  --privileged=true eeb6ee3f44bd /usr/sbin/init

 python manage.py runserver 0:8080
docker build -t opencv-webcam .
docker run -it -v $PWD:/app/ --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY opencv-webcam bash