#!/usr/bin/env python3
# 2018-10-21 (cc) <paul4hough@gmail.com>

import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# fixme - don't repeat this line
with open("../../../defaults/main.yaml", 'r') as stream:
    defaults = yaml.load(stream)


def test_admin_tcp_port(host):
    port = host.socket("tcp://0.0.0.0:%d" %
                       defaults.influxdb_admin.bind_port)
    assert port.is_listening


def test_http_tcp_port(host):
    port = host.socket("tcp://0.0.0.0:%d" %
                       defaults.influxdb_http.bind_port)
    assert port.is_listening
