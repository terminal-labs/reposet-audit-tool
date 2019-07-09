useradd -m vagrant
mkdir -p /home/vagrant
touch /home/vagrant/.bashrc

echo vagrant ALL=NOPASSWD:ALL > /etc/sudoers.d/vagrant

mkdir -p /vagrant
cp -a /home/circleci/repo/. /vagrant/
chown -R vagrant /vagrant 
