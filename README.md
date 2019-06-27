# Openshift Client Deployment

The goal is to be able to automatically deploy a service that provides oc clients for linux, windows and mac OS.

## Installation via Ansible

```[bash]
ansible-playbook playbook.yml \
                 -e "openshift_client_distributor_namespace=appuio-infra" \ 
                 -e  "openshift_client_distributor_name=openshift-client-distributor" \
                 -e  "openshift_client_distributor_hostname=client-test.example.com"
```

## Known Issues
NodeSelector needs to be set manually:
```
oc patch daemonset openshift-client-distributor -p '{"spec":{"template":{"spec":{"nodeSelector":{"node-role.kubernetes.io/master": "true"}}}}}' \
```

## Parameters
| Parameter  | Description | Defaults |
| ------------- | ------------- | ------------- |
| openshift_client_distributor_name | Name of the DaemonSet to Create | openshift-client-distributor |
| openshift_client_distributor_hostname | Set the hostname to serve the files | - |
| openshift_client_distributor_namespace | Name of the Namespace where to deploy the Daemonset | - |
