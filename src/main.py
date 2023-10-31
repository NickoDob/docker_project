from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get

NORNIR_CONFIG_FILE = "nornir_config.yaml"

nr = InitNornir(config_file=NORNIR_CONFIG_FILE)


def get_host_data(task):
    task.run(
        task=napalm_get,
        getters=['facts', 'lldp_neighbors_detail']
    )


get_host_data_result = nr.run(get_host_data)

for device, result in get_host_data_result.items():
    print(f'{device} failed: {result.failed}')