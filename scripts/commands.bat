docker build -t hostile-tweets-app .

docker tag hostile-tweets-app default-route-openshift-image-registry.apps.<cluster-domain>/<project>/hostile-tweets-app:latest
docker push default-route-openshift-image-registry.apps.<cluster-domain>/<project>/hostile-tweets-app:latest

oc delete deployment hostile-tweets-app --ignore-not-found
oc delete service hostile-tweets-service --ignore-not-found
oc delete route hostile-tweets-route --ignore-not-found
oc delete configmap hostile-tweets-config --ignore-not-found
oc delete secret hostile-tweets-secrets --ignore-not-found

oc apply -f infra/configmap.yaml
oc apply -f infra/secrets.yaml

oc apply -f infra/deployment.yaml
oc apply -f infra/service.yaml
oc apply -f infra/route.yaml

oc get pods
oc get route hostile-tweets-route