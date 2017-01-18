#!/usr/bin/python
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.gce import gce_connect

DOCUMENTATION = '''
---
module: gce_snapshot
version_added: "2.2"
short_description: manage GCE instance snapshots
description:
    - Manages GCE instance snapshots.
options:
requirements: [ "apache-libcloud" ]
author: CloudOne <devops@oncloudone.com>
'''

EXAMPLES = '''
'''

try:
    from libcloud.compute.types import Provider
    _ = Provider.GCE
    HAS_LIBCLOUD = True
except ImportError:
    HAS_LIBCLOUD = False


def find_snapshot(volume, name):
    found = None
    snapshots = volume.list_snapshots()
    for snapshot in snapshots:
        if name == snapshot.name:
            found = snapshot
    return found


def main():
    module = AnsibleModule(
        argument_spec=dict(
            instance_name=dict(required=True, type='str'),
            snapshot_name=dict(required=True, type='str'),
            state=dict(choices=['present', 'absent'], default='present'),
            service_account_email=dict(type='str'),
            credentials_file=dict(type='path'),
            project_id=dict(type='str')
        )
    )

    if not HAS_LIBCLOUD:
        module.fail_json(msg='libcloud is required for this module')

    gce = gce_connect(module)

    instance_name = module.params.get('instance_name')
    snapshot_name = module.params.get('snapshot_name')
    state = module.params.get('state')

    msg = ''
    changed = False

    instance = gce.ex_get_node(instance_name, 'all')
    disks = instance.extra['disks']

    for disk in disks:
        device_name = disk['deviceName']
        volume_obj = gce.ex_get_volume(device_name)
        snapshot = find_snapshot(volume_obj, snapshot_name)

        if snapshot and state == 'present':
            msg = snapshot_name + " already exists"

        elif snapshot and state == 'absent':
            snapshot.destroy()
            changed = True
            msg = snapshot_name + " was deleted"

        elif not snapshot and state == 'present':
            volume_obj.snapshot(snapshot_name)
            changed = True
            msg = snapshot_name + ' created'

        elif not snapshot and state == 'absent':
            msg = snapshot_name + " already deleted"

    module.exit_json(msg=msg, changed=changed)


main()
