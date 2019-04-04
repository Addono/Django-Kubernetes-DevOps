# Django Kubernetes CICD
Deploys a simple Django project onto a Kubernetes cluster using Gitlab CI.

The Gitlab deployment pipeline is based of the Auto DevOps script supplied by Gitlab.

## Getting Started

1. Fork this repository on any Gitlab instance.
2. Add a Kubernetes cluster under Operations > Kubernetes.
3. Install the following applications: Helm, Ingress and Cert-Manager.
4. Create a wildcard DNS entry to the Ingress Endpoint - it might take a while before this is resolved.
5. Set the Gitlab CI variable `AUTO_DEVOPS_DOMAIN` to your wildcard domain, this can be achieved in several ways, one would be to replace the variable value in `.gitlab-ci.yml` and commit it, or overwrite this value by adding it under Settings > CI / CD > Environment variables.
6. Ensure that a new deployment is triggered after the domain is configured. If you added a new commit, then this should be done automatically. Otherwise, go to CI / CD > Pipelines and create a new pipeline for `master`.

