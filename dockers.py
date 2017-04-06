#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import subprocess


class Docker(object):
    # container status: running,restarting, exited
    def __init__(self):
        pass

    @classmethod
    def restart_containers(self):
        containers = self.list_of_containers()
        for container in containers:
            if 'rabbitmq' in container:
                continue
            subprocess.call(["docker restart %s" % container], shell=True)
    
    @classmethod
    def remove_none_images(self):
        subprocess.call(["docker rmi $(docker images | grep \"^<none>\" | awk '{print $3}')" ], shell=True)

    @staticmethod
    def remove_all_containers():
        subprocess.call(["docker rm -f $(docker ps -qa)"], shell=True)

    @staticmethod
    def remove_all_volumes():
        subprocess.call(["docker volume rm $(docker volume ls)"], shell=True)

    @classmethod
    def rebuild_and_recompose(self):
        subprocess.call(["docker-compose up -d --build"], shell=True)

    @classmethod
    def build(self):
        # type: () -> object
        subprocess.call(["docker-compose build"], shell=True)

    @classmethod
    def compose_up(self):
        # type: () -> object
        subprocess.call(["docker-compose up -d"], shell=True)

    @classmethod
    def check_status(self):
        containers = self.list_of_containers()
        containers_status = {}
        for container in containers:
            status = subprocess.Popen(
                ["docker inspect -f {{.State.Status}} %s" % container],
                shell=True,
                stdout=subprocess.PIPE
            ).communicate()[0]
            containers_status[container] = True if status.strip() == 'running' else False
        print containers_status
        return containers_status

    @staticmethod
    def list_of_containers():
       containers = subprocess.Popen(
           ["docker inspect --format='{{.Name}}' $(docker ps -qa --no-trunc)"],
           shell=True,
           stdout=subprocess.PIPE
       ).communicate()[0]
       return [i[1:] for i in containers.split('\n') if i]


def main():
   if len(sys.argv) < 2:
       print 'No action specified.'
       sys.exit()
   else:
       option = sys.argv[1]
       if option == 'rmall':
           #删除所有数据卷与容器
           Docker.remove_all_containers()
           Docker.remove_all_volumes()
       elif option == 'rmv':
           #删除所有数据卷
           Docker.remove_all_volumes()
       elif option == 'rmi':
           Docker.remove_none_images()
       elif option == 'update':
           #领docker-compose.yml生效
           Docker.compose_up()
       elif option == "rmc":
           #删除所有容器
           Docker.remove_all_containers()
       elif option == 'rebuild':
           #删除所有数据与容器,重新运行项目
           print 'removing all containers'
           Docker.remove_all_containers()
           print "removing all volumes"
           Docker.remove_all_volumes()
           print "recomposing "
           Docker.rebuild_and_recompose()
       elif option == 'status':
           Docker.check_status()
       else:
           print 'Unknown option.'
           sys.exit()


if __name__=="__main__":
   main()
