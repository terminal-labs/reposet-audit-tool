export PY_ENV_VERSION=3.6.6
export SERVICE_USER=vagrant

PATH=/home/${SERVICE_USER}/.pyenv/bin:$PATH

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv install -s ${PY_ENV_VERSION}
pyenv global ${PY_ENV_VERSION}
pyenv global
