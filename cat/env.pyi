def get_supported_env_variables(): ...
def fix_legacy_env_variables() -> None: ...
def get_env(name):
    '''Utility to get an environment variable value. To be used only for supported Cat envs.
    - covers default supported variables and their default value
    - automagically handles legacy env variables missing the prefix "CCAT_"
    '''
