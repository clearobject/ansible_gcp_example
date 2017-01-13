Introduction
===

This project provides a set of examples for managing GCE instances. These
examples were built for the Indianapolis Ansible meetup. If you'd like to test
these examples out on your own, you may want to change the various vars in the
playbooks for your own needs.

Inventory
===

Inventory files are pulled from the contrib/inventory directory in Ansible. In
order to access the specific account, you will need to set three values.

* GCE_PROJECT # Project ID
* GCE_EMAIL # Service account email
* GCE_PEM_FILE_PATH # GCE Generated credentials JSON

These can be be set in the gce.ini, in a secrets.py file, or in your environment

In order to SSH into the instances, you will need to connect once with the
gcloud tool in order to generate a key in $HOME/.ssh/google_compute_engine

Executing a Playbook
===

```
ansible-playbook -i inventory/gce.py playbooks/<playbook_name>
```

Available Playbooks
===
name | description
--- | ---
provision | Creates two instances gcpdemo0 and gcpdemo1
teardown | Deletes GCP demo instances
nginx | Installs nginx on target servers and opens port 80
dns | Adds a dns zone and dns entry for one of the instances
image | Creates a persistent disk resource and a disk image
load_balancer | Creates a load balancer that sets up health checks
storage | Creates an object bucket, adds and object, and retrieves it
