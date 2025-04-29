# AGGREGATE Management Role

This Ansible role is designed to manage aggregate on NetApp ONTAP systems.

## Documentation

For detailed information on how to use modules, please refer to the official Ansible documentation. [Link](https://docs.ansible.com/ansible/latest/collections/netapp/ontap/index.html)

main.yml
- not used yet

get_best_aggregate.yml
- `include role rest`

The role uses the following variables:

**get_best_aggregate.yml**

| Variable              | Default | Description                              |
|-----------------------|---------|------------------------------------------|
| `cluster_name`        |         | for module variable `hostname`           |
| `netapp_username`     |         | for module variable `username`           |
| `netapp_password`     |         | for module variable `password`           |
| `validate_certs`      |         | for module variable `validate_certs`     |
