vagrant up
vagrant ssh --command 'cd /vagrant; sudo bash install_prereqs.sh'
vagrant ssh --command 'cd /vagrant; sudo bash install_python.sh'
vagrant ssh --command 'cd /vagrant; sudo bash install_pip_requirements.sh'
