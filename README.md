# Ansible Collection - sgs.ontap

[![Build Status](https://dev.azure.com/swatchgroupservices-itsi/Ansible%20Collections/_apis/build/status/sgs.ontap?branchName=main)](https://dev.azure.com/swatchgroupservices-itsi/Ansible%20Collections/_build/latest?definitionId=4&branchName=main)
![version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=git&logoColor=white)

This collection provides a series of Ansible modules used by Swatch Group Services.

## Getting Started

To install `sgs.ontap` collection:

- Create a `requirements.yml` file

```yaml
collections:
  - name: sgs.ontap
    source: git@ssh.dev.azure.com:v3/swatchgroupservices-itsi/Ansible%20Collections/sgs.ontap
    type: git
    version: 1.0.0
```

- Install collection with `ansible-galaxy`

```bash
ansible-galaxy install -r requirements.yml
```

## Testing

You have to check out the repository into a specific path structure to be able to run `ansible-test`. The path to the git checkout must end with `{...}/ansible_collections/{namespace}/{collection}/`.

```bash
mkdir -p ~/dev/ansible_collections/sgs
git clone 'git@ssh.dev.azure.com:v3/swatchgroupservices-itsi/Ansible%20Collections/sgs.ontap' ~/dev/ansible_collections/sgs/ontap
cd ~/dev/ansible_collections/sgs/ontap
```

We are using `poetry` to manage Python dependencies so you need to have poetry installed to test the collection.

> To setup your Python environment check out the documentation on [FindIt](https://findit.swatchgroup.net/x/DYSaC).

Once `poetry` is installed you can install dependencies:

```bash
poetry install
```

We are using `nox` to manage our test sequences:

```bash
# List every tests available
poetry run nox -l
# Run every tests
poetry run nox
```

If you want to run a specific test:

```bash
poetry run nox -s <session>
```

For example:

```bash
# To run only unit tests for python 3.10
poetry run nox -s "unit(python='3.10')"
# To run only sanity tests for every python version
poetry run nox -s sanity
```

### Local testing

To test a module locally without `ansible-test` we need to update Python path.
You can simply run the `run_module.sh` script with the module name you want to test in parameter:

```bash
tests/utils/run_module.sh <module_name>
# Example for hello_world module
tests/utils/run_module.sh hello_world
```

This is required only if you want to test a module that have import from `module_utils`. If your module have no internal import you can launch the module without modifying Python path:

```bash
poetry run python3 plugins/modules/<module_name>.py plugins/args/<module_name>.json
# Example for hello_world module
poetry run python3 plugins/modules/hello_world.py plugins/args/hello_world.json
```

> You need to have a json file that contains the arguments for the module you want to test. Every `args.json` files are located in `plugins/args/`.
> For module that need credentials please update the associated `json` file.

### Sanity tests

The following example commands expect that you have installed Docker or Podman.
> Note that Podman has only been supported by more recent ansible-core releases. If you are using Docker, the following will work with Ansible 2.9+.

To perform sanity tests:

```bash
# Run sanity tests for all files in the collection:
poetry run ansible-test sanity --docker -v

# Run sanity tests for the given files
poetry run ansible-test sanity --docker -v plugins/modules/hello_world.py

# Run sanity tests for one Python version:
poetry run ansible-test sanity --docker --python 3.9 -v
```

> You can fix almost any lint issue by running `poetry run black .`.

### Unit tests

The following commands show how to run unit tests:

```bash
# Run all unit tests:
poetry run ansible-test units --docker --coverage

# Run all unit tests for one Python version (a lot faster):
poetry run ansible-test units -v --docker --coverage --python 3.9

# Run a specific unit test (here hello_world module):
poetry run ansible-test units --docker --coverage -v tests/unit/plugins/modules/test_hello_world.py
```

> Currently there is no mechanism to run unit tests for Powershell modules.

### Coverage

```bash
# Getting coverage report
poetry run ansible-test coverage report --show-missing --include 'plugins/*/*'
```

To clear data between test runs, just remove `output` folder.

```bash
rm -r tests/output
```

### Integration tests

The following commands show how to run integration tests:

You can list available integration tests:

```bash
poetry run ansible-test integration --list
```

To run integration tests for the 'hello_world' module in a Docker container:

```bash
poetry run ansible-test integration --docker -v hello_world
```
