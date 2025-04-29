# LUN Management Role

This Ansible role is designed to manage LUNs on NetApp ONTAP systems.

## Documentation

For detailed information on how to use modules, please refer to the official Ansible documentation. [Link](https://docs.ansible.com/ansible/latest/collections/netapp/ontap/index.html)

main.yml
- `netapp.ontap.na_lun`

map.yml
- `netapp.ontap.na_ontap_lun_map`

The role uses the following variables:

**main.yml**
more is coming soon. Stay tuned.

| Variable              | Default | Description                              |
|-----------------------|---------|------------------------------------------|
| `cluster_name`        |         | for module variable `hostname`           |
| `netapp_username`     |         | for module variable `username`           |
| `netapp_password`     |         | for module variable `password`           |
| `validate_certs`      |         | for module variable `validate_certs`     |
| `state`               | present | for module variable `state`              |
| `vserver`             |         | for module variable `vserver`            |
| `flexvol_name`        |         | for module variable `flexvol_name `      |
| `name`                |         | for module variable `name`               |
| `size`                |         | for module variable `size`               |
| `size_unit`           | gb      | for module variable `size_unit`          |
| `os_type`             | omit    | for module variable `os_type`            |
| `qtree_name`          | omit    | for module variable `qtree_name`         |
| `space_allocation`    | omit    | for module variable `space_allocation`   |
| `space_reserve`       | omit    | for module variable `space_reserve`      |

**map.yml**

| Variable              | Default | Description                               |
|-----------------------|---------|-------------------------------------------|
| `cluster_name`        |         | for module variable `hostname`            |
| `netapp_username`     |         | for module variable `username`            |
| `netapp_password`     |         | for module variable `password`            |
| `validate_certs`      |         | for module variable `validate_certs`      |
| `state`               | present | for module variable `state`               |
| `initiator_group_name`|         | for module variable `initiator_group_name`|
| `path`                |         | for module variable `path`                |
| `vserver`             |         | for module variable `vserver`             |
| `lun_id`              | omit    | for module variable `lun_id`              |
