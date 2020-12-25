# -*- mode: ruby -*-
# vi: set ft=ruby :

$installer = <<-INSTALLER
yum -y install epel-release
yum -y install rabbitmq-server
systemctl start rabbitmq-server
systemctl restart rabbitmq-server
systemctl enable rabbitmq-server
rabbitmqctl add_user testuser testpassword
rabbitmqctl add_vhost worker
rabbitmqctl set_permissions -p worker testuser ".*" ".*" ".*"
firewall-cmd --zone=public --add-port=5672/tcp
firewall-cmd --zone=public --add-port=5672/tcp --permanent
INSTALLER


Vagrant.configure("2") do |config|
  default_url              = "http://mirror.hostnet.nl/vagrant"
  default_archs            = [ "x86_64" ]
  default_domain           = "vagrant.hostnetbv.nl"
  default_binary_path      = "/opt/puppetlabs/bin"
  default_puppet_options   = "--verbose --debug"
  default_environment_path = "vagrant"
  default_module_path      = [ "modules", "vendor" ]

  boxes = {
    'centos7' => {
      'name'  => 'centos_7',
    },
  }

  boxes.each do |imgname, params|
    url_root         = params['url_root']         || default_url
    archs            = params['archs']            || default_archs
    domain           = params['domain']           || default_domain
    name             = params['name']             || imgname
    archs.each do |arch|
      boxname        = params['boxname']          || "#{name}_#{arch}"
      environment    = params['environment']      || boxname
      hostname       = "#{imgname}-#{arch}".tr('_','-')
      config.vm.define boxname.to_sym do |box|
        box.vm.network "forwarded_port", guest: 5672, host: 5672
        box.vm.box = "#{imgname}-#{arch}"
        box.vm.box_url = "#{url_root}/#{imgname}-#{arch}"
        box.vm.hostname = "#{hostname}.#{domain}"
        box.vm.provision "shell", inline: $installer
      end
    end
  end
end

