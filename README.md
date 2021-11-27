# ecs Prerequisites

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
