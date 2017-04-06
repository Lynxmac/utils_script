# utils_script
Some useful scripts


### install_docker_and_docker_compose.sh
功能：
- ubuntu 14.04 下一键安装docker和docker-compose
使用:
- chmod +x install_docker_and_docker_compose.sh
- ./install_docker_and_docker_compose.sh


### dockers.py
#### 部分功能需安装docker-compose
功能：
- docker组合拳
用法：
- 复制到/usr/local/bin/目录下，改名为dockers：　mv dockers.py /usr/local/bin/dockers
- 添加可执行权限：　chmod +x /usr/local/bin/dockers
- 删除所有docker容器：　dockers rmc
- 清理所有none镜像：　dockers rmi
- 删除所有数据卷：　dockers rmv
- 删除所有docker容器与所有数据卷：　dockers rmall
- 彻底清理docker容器与数据卷并重新运行整个项目: dockers rebuild
- 生效docker-compose.yml: dockers update
- 重启所有容器： dockers restart
