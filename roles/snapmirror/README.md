# Snapmirror Management Role

This Ansible role is designed to manage snapmirrors on NetApp ONTAP systems.

## Documentation

For detailed information on how to use modules, please refer to the official Ansible documentation. [Link](https://docs.ansible.com/ansible/latest/collections/netapp/ontap/index.html)

main.yml
- `netapp.ontap.na_ontap_snapmirror`

## Variables

The role uses the following variables:

**main.yml**

| Variable              | Default | Description                                    |
|-----------------------|---------|------------------------------------------------|
| `destination_hostname`|         | for module variable `hostname`                 |
| `netapp_username`     |         | for module variable `username`                 |
| `netapp_password`     |         | for module variable `password`                 |
| `validate_certs`      |         | for module variable `validate_certs`           |
| `state`               | present | for module variable `state`                    |
| `source_path`         |         | for module variable `source_endpoint.path`     |
| `destination_path`    |         | for module variable `destination_endpoint.path`|
| `source_hostname`     | omit    | for module variable `source_hostname`          |
