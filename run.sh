#!/bin/bash

# add minio helm charts repo
helm repo add minio https://charts.min.io/

# deploy minio standalone with small hardware requirements
helm install --namespace default --set rootUser=rootuser,rootPassword=rootpass123 -f minio/values.yaml --generate-name minio/minio

# export ports
kubectl port-forward service/minio-1641933279 9000:9000 --namespace default &
kubectl port-forward service/minio-1641933279-console 9001:9001 --namespace default &

