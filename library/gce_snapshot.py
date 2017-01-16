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


def main():
    module = AnsibleModule(
        argument_spec=dict(
            # TODO
        )
    )

    # TODO
    exists = None
    state = None

    if exists and state == 'present':
        pass
    elif exists and state == 'absent':
        pass
    elif not exists and state == 'present':
        pass
    elif not exists and state == 'absent':
        pass

    module.exit_json()


main()
