#!/usr/bin/env python3
import os
import sys
def Clear():
    cls = ("clear")
    os.system(cls)
ARGUMENT = sys.argv[1]
if ARGUMENT == "apply":
    Clear()
    print("Sit back and Relax ECS Cluster is being Deployed !!")
    ecsCluster = ("aws cloudformation create-stack \
            --stack-name ecs-ec2 \
            --capabilities CAPABILITY_IAM \
            --template-body file://./ecs-ec2-via-cloudformation.yml")
    os.system(ecsCluster)
elif ARGUMENT == "destroy":
    Clear()
    print("!! Sit back and Relax ECS Cluster is being Destroyed !!")
    delete = ("aws cloudformation delete-stack --stack-name ecs-ec2")
    os.system(delete)
else:
    print("The usage of script: " + sys.argv[0] + " apply/destroy")
