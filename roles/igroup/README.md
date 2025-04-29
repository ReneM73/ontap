# IGROUP Management Role

This Ansible role is designed to manage igroups on NetApp ONTAP systems.

## Documentation

For detailed information on how to use modules, please refer to the official Ansible documentation. [Link](https://docs.ansible.com/ansible/latest/collections/netapp/ontap/index.html)

main.yml
- `netapp.ontap.na_ontap_igroup`

The role uses the following variables:

**main.yml**

| Variable                | Default | Description                                 |
|-------------------------|---------|---------------------------------------------|
| `cluster_name`          |         | for module variable `hostname`              |
| `netapp_username`       |         | for module variable `username`              |
| `netapp_password`       |         | for module variable `password`              |
| `validate_certs`        |         | for module variable `validate_certs`        |
| `state`                 | present | for module variable `state`                 |
| `vserver `              |         | for module variable `vserver`               |
| `name`                  |         | for module variable `name `                 |
| `force_remove_initiator`| false   | for module variable `force_remove_initiator`|
| `initiator_group_type`  | omit    | for module variable `initiator_group_type`  |
| `initiator_names`       | omit    | for module variable `initiator_names`       |
| `os_type`               | omit    | for module variable `sos_typetate`          |
