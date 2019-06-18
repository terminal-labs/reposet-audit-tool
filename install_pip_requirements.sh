su -m vagrant <<'EOF'
export PY_ENV_VERSION=3.6.6
export SERVICE_USER=vagrant
export PYENV_ROOT="/home/vagrant/.pyenv"
export PATH="${PYENV_ROOT}/bin:${PATH}"
export USE_GIT_URI="true"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv install -s ${PY_ENV_VERSION}
pyenv global ${PY_ENV_VERSION}
pyenv global

pip install -r requirements.txt
EOF
