#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2022, Swatch Group Services LTD
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.0",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: hello_world
short_description: A module that says hello in many languages
version_added: "1.0.0"
description:
  - "A module that says hello in many languages."
options:
    name:
        description:
          - Name of the person to salute. If no value is provided the default
            value will be used.
        required: false
        type: str
        default: John Doe
author:
    - Gianni Salinetti (@giannisalinetti)
"""

EXAMPLES = """
# Pass in a custom name
- name: Say hello to Linus Torvalds
  hello_world:
    name: "Linus Torvalds"
"""

RETURN = """
fact:
  description: Hello string
  type: str
  sample: Hello John Doe!
  returned: always
"""

import random

from ansible.module_utils.basic import AnsibleModule

# from ansible_collections.sgs.core.plugins.module_utils import wfhub

FACTS = [
    "Hello {name}!",
    "Bonjour {name}!",
    "Hola {name}!",
    "Ciao {name}!",
    "Hallo {name}!",
    "Hei {name}!",
]

module_args = dict(name=dict(type="str", default="John Doe"))


def setup_module_object(support_check_mode=True):
    module = AnsibleModule(
        argument_spec=module_args, supports_check_mode=support_check_mode
    )
    return module


def run_module(module):
    result = dict(changed=False, fact="")
    result["fact"] = random.choice(FACTS).format(name=module.params["name"])
    # result["test"] = wfhub.wfhub_test()
    return result


def main():
    module = setup_module_object()
    return_dict = run_module(module)
    module.exit_json(**return_dict)


if __name__ == "__main__":  # pragma: no cover
    main()
