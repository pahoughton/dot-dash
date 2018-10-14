#!/usr/bin/env python3
# 2018-10-14 (cc) <paul4hough@gmail.com>

# import sys
# import os
# import subprocess as sp

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

    # host.socket("unix:///var/run/docker.sock").is_listening
    # This HTTP server listen on all ipv4 adresses but not on ipv6
    # host.socket("tcp://0.0.0.0:80").is_listening
    # host.socket("tcp://:::80").is_listening
    # host.socket("tcp://80").is_listening
def test_interface(host):
    # do better ... fixme
    assert host.socket("tcp://0.0.0.0:80").is_listening
