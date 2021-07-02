minikube start
eval $(minikube -p minikube docker-env)
docker build -f Dockerfile -t python-docker:latest .
kubectl delete -f /home/pvips-guest/Desktop/Devops_Flow/Devops-Flow-Python/deployment.yaml 
kubectl create -f /home/pvips-guest/Desktop/Devops_Flow/Devops-Flow-Python/deployment.yaml