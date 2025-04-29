from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.sgs.ontap.plugins.modules import hello_world
from ansible_collections.sgs.ontap.tests.unit.plugins.modules.utils import (
    AnsibleExitJson,
    ModuleTestCase,
    set_module_args,
)


class TestHelloWorld(ModuleTestCase):
    def test_hello_world_main(self):
        set_module_args({"name": "Test"})

        with self.assertRaises(AnsibleExitJson) as result:
            hello_world.main()
        self.assertFalse(result.exception.args[0]["changed"])
        fact = result.exception.args[0]["fact"].split(" ")
        self.assertIn(fact[0], ["Hello", "Bonjour", "Hola", "Ciao", "Hallo", "Hei"])
        self.assertEqual(fact[1], "Test!")
