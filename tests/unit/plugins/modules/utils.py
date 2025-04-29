from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import unittest

# From Python 3.3 onwards, unittest.mock is included in the standard library
# and can be imported directly. For earlier versions, we use the mock package.
# This allows us to use the same code for both Python 2 and 3.
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from ansible.module_utils import basic
from ansible.module_utils.common.text.converters import to_bytes


# This function is used to set the arguments to the AnsibleModule
def set_module_args(args):
    # Avoir keep ansible temporary files for tests
    if "_ansible_remote_tmp" not in args:
        args["_ansible_remote_tmp"] = "/tmp"
    if "_ansible_keep_remote_files" not in args:
        args["_ansible_keep_remote_files"] = False

    # Convert the arguments to a JSON string
    args = json.dumps({"ANSIBLE_MODULE_ARGS": args})
    # Set the arguments to the AnsibleModule
    basic._ANSIBLE_ARGS = to_bytes(args)


class AnsibleExitJson(Exception):
    pass


class AnsibleFailJson(Exception):
    pass


# This function is used to simulate a successful module execution
def exit_json(*args, **kwargs):
    # if "changed" not in kwargs:
    #     kwargs["changed"] = False
    raise AnsibleExitJson(kwargs)


# This function is used to simulate a module failure
def fail_json(*args, **kwargs):
    kwargs["failed"] = True
    raise AnsibleFailJson(kwargs)


class ModuleTestCase(unittest.TestCase):
    def setUp(self):
        # Patch the AnsibleModule.exit_json and fail_json functions
        self.mock_module = patch.multiple(
            basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json
        )
        # Activate AnsibleModule patch and return a mock object
        self.mock_module.start()
        # Patch the time.sleep function to avoid waiting in the tests
        self.mock_sleep = patch("time.sleep")
        # Activate time.spleep patch and return a mock object
        self.mock_sleep.start()
        # Set default Ansible Module arguments to an empty dictionary
        set_module_args({})
        # Cleanup patches
        self.addCleanup(self.mock_module.stop)
        self.addCleanup(self.mock_sleep.stop)
