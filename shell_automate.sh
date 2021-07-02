minikube start
eval $(minikube -p minikube docker-env)
docker build -f Dockerfile -t python-docker:latest .
kubectl delete -f /home/bhavesh/Desktop/Devops-Flow-Python-main/deployment.yaml
kubectl create -f /home/bhavesh/Desktop/Devops-Flow-Python-main/deployment.yaml