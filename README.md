
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
