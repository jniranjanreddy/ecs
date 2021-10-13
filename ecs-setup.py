#!/usr/bin/env python3
import sys
import os
ARGUMENT = sys.argv[1]
if ARGUMENT == "apply":
    infra = ("aws cloudformation create-stack \
        --capabilities CAPABILITY_IAM \
        --stack-name ecs-core-infrastructure \
        --template-body file://./core-infrastructure-setup.yml")
elif ARGUMENT == "destroy":
    print("!! Sit back and Relax ECS Cluster is being Destrpyed !!")
else:
    print("The usage of script:" sys.argv[1] + "apply/destroy")