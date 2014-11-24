#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2014, Aaron Paxson <aj@thepaxson5.org>
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: hp_imc
short_description: Performs monitoring, provisioning, and configuration functions inside HP IMC for the device
description:
  - The M(hp_imc_monitoring) module currently has two basic functions: Unmanage/Manage a device to prevent notifications or polling during scheduled maintenance.
  - This module can also auto-provision a new device into IMC.
  - All actions require either I(hostname) parameter, or the I(dev_id) parameter.
  - In playbooks you can use the C({{inventory_hostname}}) or the C({{ansible_default_ipv4.address}}) variable to refer to the I(hostname) the playbook is currently running on.
  - When using the M(hp_imc_monitoring) module you will need to specify your IMC Master server using the I(imc_host) parameter.
  - The I(imc_user) and I(imc_pass) refer to a user account that has permissions for the action being performed.
version_added: "0.1"
options:
  action:
    description:
      - Action to take.
    required: true
    default: null
    choices: [ "unmanage", "manage", "provision" ]
  hostname:
    description:
      - IP Address or name of the host to run action on.
    required: false
    default: null
  dev_id:
    description:
      - Device ID of the host in IMC
    required: false
    default: null
  imc_host:
    description:
      - IMC Master server managing the device.  IP Addresses or fully-qualifed name accepted.
    required: true
    default: null
  imc_user:
    description:
      - Username with permissions for action on IMC Master server.
    required: true
    default: admin
  imc_pass:
    description:
      - Password for IMC Username
    required: true
    default: null


author: Aaron Paxson <aj@thepaxson5.org>
requirements: [ "HP Intelligent Management Center eAPI" ]
'''

EXAMPLES = '''
# Unmanage a device to prevent notices
- hp_imc_monitoring: action=unmanage hostname={{ inventory_hostname }} imc_host=1.2.3.4 imc_user=admin imc_pass=pass

# Unmanage a device using IMC Device ID
- hp_imc_monitoring: action=unmanage dev_id=516 imc_host=1.2.3.4 imc_user=admin imc_pass=pass

# Manage a device that is previously unmanaged
- hp_imc_monitoring: action=manage hostname={{ inventory_hostname }} imc_host=1.2.3.4 imc_user=admin imc_pass=pass

# Manage a device that is previously unmanaged using the fact: Default IPv4 Address variable
- hp_imc_monitoring: action=manage hostname={{ansible_default_ipv4.address}} imc_host=1.2.3.4 imc_user=admin imc_pass=pass

'''

def main():
    ACTION_CHOICES = [
        'manage',
        'unmanage',
        'provision',
        ]

    module = AnsibleModule(
        argument_spec=dict(
            action=dict(required=True, default=None, choices=ACTION_CHOICES),
            imc_user=dict(required=True, default='admin'),
            imc_host=dict(required=True, default=None),
            imc_pass=dict(required=True, default='admin'),
            hostname=dict(required=False, default=None),
            dev_id=dict(required=False, default=None),
            )
        )

    action = module.params['action']
    imc_user = module.params['imc_user']
    imc_host = module.params['imc_host']
    imc_pass = module.params['imc_pass']
    hostname = module.params['hostname']
    dev_id = module.params['dev_id']

import urllib2


class IMCServer(object):
    # Build the server class to setup connections
    hostname = 'usnassrv53.cd.corp'

    def isManaged(self):
    # Check if system is currently managed or not
        return

    def isProvisioned(self):
    # Check if the system is currently provisioned or not
        return
