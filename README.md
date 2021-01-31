# yandex.praktikum-alghoritms
Practice for Algorithm Course in Yandex.Praktikum

# Python Installation

Install python version manager

https://github.com/pyenv/pyenv

https://github.com/pyenv/pyenv-virtualenv


## Python Version Setup

```shell
# Install interpreter version
pyenv install 3.7.9

# Install Separate Virtualenv
pyenv virtualenv 3.7.9 yandex-praktukum-python3.7.9

# Activate
pyenv activate yandex-praktukum-python3.7.9

# Install Requirement
pip install -r requirement.txt
```

## Install new dependency

```shell
pip install <name> && pip freeze | grep <name> >> requirements.txt
```

