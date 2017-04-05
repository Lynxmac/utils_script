#!/bin/bash

Install_docker(){
        docker -v
        local docker_version=$?
        if [[ "$docker_version" -eq  0 ]]; then
                echo "docker already install"
        elif [[ "$docker_version" -eq 127 ]];then
                apt-get update
                apt-get install -y linux-image-generic-lts-trusty
                apt-get install -y curl
                curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -
                echo "DOCKER_OPTS=\"\$DOCKER_OPTS --registry-mirror=https://vl3t60ea.mirror.aliyuncs.com\"" | sudo tee -a /etc/default/docker
                sudo service docker restart
        fi


}



Install_docker_compose(){
        echo "testing the network..."
        if [[ $(ping -c4 -nq www.google.com | awk -F"/" '/rtt/{print int($5)}') == "" ]]; then
                echo "There is a networking issue,use the proxy..."
                proxy="-x us.centos.bz:31281"
        fi
        curl -L $proxy  "https://github.com/docker/compose/releases/download/1.11.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        chmod +x /usr/local/bin/docker-compose
        docker-compose --version
}

Install_docker
Install_docker_compose
