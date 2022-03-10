# ecs Prerequisites
#append to .bashrc
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] # "






What roles required for ECS.
1. EC2Role
2. ECSRole
3. ECSTaskExecutionRole
4. AutoscalingRole

Create Fargate Cluster: -
```
[root@minikube01 python-flask-training]# aws ecs create-cluster --cluster-name dev-fargate
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:ap-south-1:936766936551:cluster/dev-fargate",
        "clusterName": "dev-fargate",
        "status": "ACTIVE",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "statistics": [],
        "tags": [],
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ],
        "capacityProviders": [],
        "defaultCapacityProviderStrategy": []
    }
}
```
Delete fargate Cluster:-
```
[root@minikube01 python-flask-training]# aws ecs delete-cluster --cluster dev-fargate
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:ap-south-1:936766936551:cluster/dev-fargate",
        "clusterName": "dev-fargate",
        "status": "INACTIVE",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "statistics": [],
        "tags": [],
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ],
        "capacityProviders": [],
        "defaultCapacityProviderStrategy": []
    }
}
(my-py3-env) [root@minikube01 python-flask-training]#
```
Create task
```
[root@minikube01 ecs]# aws ecs register-task-definition --cli-input-json file:///jnr/ecs/sleep360.json
{
    "taskDefinition": {
        "taskDefinitionArn": "arn:aws:ecs:ap-south-1:936766936551:task-definition/sleep360:1",
        "containerDefinitions": [
            {
                "name": "sleep",
                "image": "busybox",
                "cpu": 10,
                "memory": 10,
                "portMappings": [],
                "essential": true,
                "command": [
                    "sleep",
                    "360"
                ],
                "environment": [],
                "mountPoints": [],
                "volumesFrom": []
            }
        ],
        "family": "sleep360",
        "revision": 1,
        "volumes": [],
        "status": "ACTIVE",
        "placementConstraints": [],
        "compatibilities": [
            "EXTERNAL",
            "EC2"
        ],
        "registeredAt": "2021-11-27T12:09:10.249000-05:00",
        "registeredBy": "arn:aws:iam::936766936551:root"
    }
}
```
```
[root@minikube01 ecs]# cat sleep360.json
{
    "containerDefinitions": [
        {
            "name": "sleep",
            "image": "busybox",
            "cpu": 10,
            "command": [
                "sleep",
                "360"
            ],
            "memory": 10,
            "essential": true
        }
    ],
    "family": "sleep360"
}

```
```
[root@minikube01 ecs]# aws ecs list-task-definitions
{
    "taskDefinitionArns": [
        "arn:aws:ecs:ap-south-1:936766936551:task-definition/sleep360:1"
    ]
}

```
