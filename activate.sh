export APPNAME=repoaudittool
export USERNAME=user
export PLATFROM=linux
export PYENV_ROOT=/home/${USERNAME}/pyenv/envs/${APPNAME}/.pyenv
export PATH="/Users/${USERNAME}/.local/bin:${PATH}"
export PATH="${PYENV_ROOT}/bin:${PATH}"
export USE_GIT_URI="true"
eval "$(pyenv init -)"
