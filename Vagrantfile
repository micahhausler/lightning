#!/usr/bin/env ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant::VERSION >= "1.1.0" and Vagrant.configure("2") do |config|
  config.vm.box_url = "http://goo.gl/8kWkm" #  Ubuntu Server 12.04 amd64 (with Puppet, Chef and VirtualBox 4.2.1), 267MB
  config.vm.box = "ubuntu1204"


  config.vm.define :web1 do |web1_config|

    web1_config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", 1024]
    end

    # To open a port, the syntax is  guest: <vm port>, host: <host port>
    web1_config.vm.network :forwarded_port, guest: 80, host: 8080
    web1_config.vm.network :forwarded_port, guest: 8000, host: 8000
    #web1_config.vm.forward_port 22, 2222
    web1_config.vm.hostname = "web1"

    # To share a folder, the syntax is <key> (whatever you want it to be), <host path>, <vagrant path>
    #web1_config.vm.share_folder "setup", "~/setup", "./setup"
    #web1_config.vm.synced_folder "./host/folder", "/absolute/guest/folder"

    web1_config.vm.provision :shell, :path => "ubuntu_setup.sh"

  end
end

