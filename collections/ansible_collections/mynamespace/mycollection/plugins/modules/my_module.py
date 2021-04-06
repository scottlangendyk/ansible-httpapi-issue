from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection

def main():
    module = AnsibleModule(
        argument_spec = dict()
    )

    connection = Connection(module._socket_path)

    result = connection.send_request('')

    module.exit_json(changed=True, http_result=str(result))

if __name__ == '__main__':
    main()