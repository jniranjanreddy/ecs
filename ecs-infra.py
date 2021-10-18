#!/usr/bin/env python3
import os
import sys
import platform
def Clear():
    cls = ("clear")
    os.system(cls)

ARGUMENT = sys.argv[1]
if ARGUMENT == "apply":
    Clear()
    print("Sit back and Relax ECS infrastructure is being Deployed !!")
    infra = ("aws cloudformation create-stack \
        --capabilities CAPABILITY_IAM \
        --stack-name ecs-core-infrastructure \
        --template-body file://./core-infrastructure-setup.yml")
    platform.os.system(infra)
elif ARGUMENT == "destroy":
    Clear()
    print("!! Sit back and Relax ECS infrastructure is being Destroyed !!")
    delete = ("aws cloudformation delete-stack --stack-name ecs-core-infrastructure")
    platform.os.system(delete)
    
else:
    print("The usage of script: " + sys.argv[0] + " apply/destroy")