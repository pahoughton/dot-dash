# 2018-10-19 (cc) <paul4hough@gmail.com> -*- mode: ruby -*-
#


Vagrant.configure("2") do |config|
  config.vm.box_check_update = false

  hname = 'monitor'
  config.vm.define hname do |bcfg|
    bcfg.vm.box = "ubuntu/xenial64"
    bcfg.vm.hostname = hname
    bcfg.vm.network    'private_network', ip: '10.10.10.10'
    #bcfg.vm.network "forwarded_port", guest: 3000, host: 13000
    bcfg.vm.provider 'virtualbox' do |vb|
      vb.name      = hname
      vb.cpus      = 2
      vb.memory    = 2048
      vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
      vb.customize ['modifyvm', :id, '--natdnspassdomain1', 'on']
      vb.customize ['modifyvm', :id, '--usb', 'off']
    end
    bcfg.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/monitor.yml"
      ansible.extra_vars = {
        ansible_python_interpreter:"/usr/bin/python3"
      }
    end
  end
end
