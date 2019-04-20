This project is very experimental

# Installation For Development

install anaconda
```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh -b

export PATH="~/miniconda3/bin:$PATH"

rm Miniconda3-latest-Linux-x86_64.sh
```

setup conda env
```
conda create -n repo-audit-tool python=3.7

source activate repo-audit-tool
```

install
```
pip install repoaudittool
```
