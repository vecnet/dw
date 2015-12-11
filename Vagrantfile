# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  config.vm.provider :virtualbox do |vb|
            vb.name = "dw"
  end
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  # https://atlas.hashicorp.com/chef/boxes/centos-7.0/versions/1.0.0/providers/virtualbox.box
  config.vm.box = "chef/centos-7.0"


  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8000, host: 8001
  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 5432, host: 5433

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
     pwd
     # Enable EPEL repository
     sudo yum -y install http://lug.mtu.edu/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
     sudo yum -y install http://yum.postgresql.org/9.3/redhat/rhel-7-x86_64/pgdg-redhat93-9.3-2.noarch.rpm
     sudo yum -y install vim python postgresql93-server python-psycopg2 numpy
     # Necessary for django-auth-pubtkt
     sudo yum -y install openssl-devel
     sudo yum -y install postgis2_93
     sudo /usr/pgsql-9.3/bin/postgresql93-setup initdb
     sudo yum -y install vim python python-psycopg2 numpy
     sudo curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
     sudo python get-pip.py
     sudo rm get-pip.py
     sudo pip install -r /vagrant/requirements.txt
     sudo postgresql-setup initdb
     sudo systemctl enable postgresql-9.3
     sudo sh -c 'echo "local   all             all                                     peer" > /var/lib/pgsql/9.3/data/pg_hba.conf'
     sudo sh -c 'echo "host    all             all             all    md5">> /var/lib/pgsql/9.3/data/pg_hba.conf'
     sudo sh -c "echo listen_addresses = \\'*\\' >> /var/lib/pgsql/9.3/data/postgresql.conf"
     sudo systemctl start postgresql-9.3
     sudo -u postgres sh -c 'dropdb dw'
     sudo -u postgres sh -c 'createdb dw'
     sudo -u postgres psql -c "CREATE USER dw WITH PASSWORD 'dw';"
     sudo -u postgres psql -c "ALTER USER dw WITH CREATEDB;"
     sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE dw to dw;"
     sudo -u postgres psql dw -c "CREATE EXTENSION postgis;"
     sudo -u postgres psql dw -c "CREATE EXTENSION postgis_topology;"
     sudo systemctl restart postgresql-9.3

   SHELL
end
