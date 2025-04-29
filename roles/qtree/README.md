# QTREE Management Role

This Ansible role is designed to manage qtree on NetApp ONTAP systems.

## Documentation

For detailed information on how to use modules, please refer to the official Ansible documentation. [Link](https://docs.ansible.com/ansible/latest/collections/netapp/ontap/index.html)

main.yml
- `netapp.ontap.na_ontap_qtree`

The role uses the following variables:

**main.yml**

| Variable              | Default | Description                              |
|-----------------------|---------|------------------------------------------|
| `cluster_name`        |         | for module variable `hostname`           |
| `netapp_username`     |         | for module variable `username`           |
| `netapp_password`     |         | for module variable `password`           |
| `validate_certs`      |         | for module variable `validate_certs`     |
| `state`               | present | for module variable `state`              |
| `vserver`             |         | for module variable `vserver`            |
| `flexvol_name`        |         | for module variable `flexvol_name`       |
| `name`                |         | for module variable `name`               |
| `security_style`      |         | for module variable `security_style`     |
| `unix_permissions`    |         | for module variable `unix_permissions`   |
