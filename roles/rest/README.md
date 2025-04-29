# REST Role

This Ansible role is designed to gather information or execute commands via REST APIs on NetApp ONTAP systems.

## Documentation

For detailed information on how to use modules, please refer to the official Ansible documentation. [Link](https://docs.ansible.com/ansible/latest/collections/netapp/ontap/index.html)

rest.yml
- `netapp.ontap.na_ontap_rest_info`

cli.yml
- `netapp.ontap.na_ontap_rest_cli`

## Variables

The role uses the following variables:

**info.yml**

| Variable              | Default | Description                              |
|-----------------------|---------|------------------------------------------|
| `cluster_name`        |         | for module variable `hostname`           |
| `netapp_username`     |         | for module variable `username`           |
| `netapp_password`     |         | for module variable `password`           |
| `validate_certs`      |         | for module variable `validate_certs`     |
| `fields`              | omit    | for module variable `fields`             |
| `gather_subset`       | omit    | for module variable `gather_subset`      |
| `owning_resource`     | omit    | for module variable `owning_resource`    |
| `parameters`          | omit    | for module variable `parameters`         |
| `use_python_keys`     | true    | for module variable `use_python_keys`    |
| `result_var`          | omit    | to register the output                   |

**cli.yml**

| Variable              | Default | Description                              |
|-----------------------|---------|------------------------------------------|
| `cluster_name`        |         | for module variable `hostname`           |
| `netapp_username`     |         | for module variable `username`           |
| `netapp_password`     |         | for module variable `password`           |
| `validate_certs`      |         | for module variable `validate_certs`     |
| `command`             |         | for module variable `command`            |
| `verb`                |         | for module variable `verb`               |
| `body`                | omit    | for module variable `body`               |
| `params`              | omit    | for module variable `params`             |
| `result_var`          | omit    | to register the output                   |
