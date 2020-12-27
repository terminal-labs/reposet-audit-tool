import os

from repoaudittool.derived_settings import SITEPACKAGESPATH


def get_env_variable(name):
    assert isinstance(name, str) is True
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def resolve_payload_path(EGG_NAME, PROJECT_NAME):
    possible_path = SITEPACKAGESPATH + "/" + EGG_NAME + ".egg-link"
    if os.path.exists(possible_path):
        egglink_file = open(possible_path, "r")
        link_path = egglink_file.read().split("\n")[0]
        possible_payload_path = link_path + "/" + PROJECT_NAME + "/payload"
    else:
        possible_path = SITEPACKAGESPATH + "/" + PROJECT_NAME
        possible_payload_path = possible_path + "/payload"
    return possible_payload_path


def resolve_config_path(EGG_NAME, PROJECT_NAME):
    possible_path = SITEPACKAGESPATH + "/" + EGG_NAME + ".egg-link"
    if os.path.exists(possible_path):
        egglink_file = open(possible_path, "r")
        link_path = egglink_file.read().split("\n")[0]
        possible_payload_path = link_path
        return possible_payload_path + "/conf.cfg"
    else:
        possible_path = SITEPACKAGESPATH + "/" + PROJECT_NAME
        possible_payload_path = possible_path
        return possible_payload_path + "/conf.cfg"
