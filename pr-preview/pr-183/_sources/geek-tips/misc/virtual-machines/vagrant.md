# Vagrant

**Vagrant** is a wrapper for **VirtualBox**. It allows you to interact with your virtual box using a `Vagrantfile` and a set of commands, similar to Docker.

Tutorial: [https://www.youtube.com/watch?v=vBreXjkizgo](https://www.youtube.com/watch?v=vBreXjkizgo)​

## Installing <a href="installing" id="installing"></a>

1. To use **Vagrant**, you will first need to install **VirtualBox**: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)​
2. Install Vagrant from here: [https://learn.hashicorp.com/tutorials/vagrant/getting-started-index?in=vagrant/getting-started](https://learn.hashicorp.com/tutorials/vagrant/getting-started-index?in=vagrant/getting-started)​

## Getting Started & Basic Commands <a href="getting-started-and-basic-commands" id="getting-started-and-basic-commands"></a>

To create a box:

```bash
vagrant init <BOX_NAME>
```

For example:

```bash
vagrant init ubuntu/trusty64
```

To run the box:

```
vagrant up
```

To shut down the box:

```bash
vagrant suspend
```

To resume the box:

```bash
vagrant resume
```

To remove the box permanently:

```bash
vagrant destroy
```

If you update your `Vagrantfile` and want to reload:

```bash
vagrant reload
```

## SSH into Box <a href="ssh-into-box" id="ssh-into-box"></a>

You can SSH into your box:

```bash
vagrant ssh
```

This will bring up a terminal that you can use. For example, you might want to install git:

```bash
sudo apt-get update
sudo apt-get install -y git
```

## Vagrantfile <a href="vagrantfile" id="vagrantfile"></a>

### Memory and CPU Settings <a href="memory-and-cpu-settings" id="memory-and-cpu-settings"></a>

To configure memory and CPU used by your virtual box:

```ruby
config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 4
end
```

### Folder Settings <a href="folder-settings" id="folder-settings"></a>

You will probably also want to use data from your local machine. To do this:

```ruby
config.vm.synced_folder "path/to/local/folder", "path/to/vagrant/folder"
```

The `path/to/local/folder` can be absolute, or relative to the location of the Vagrantfile. The `path/to/vagrant/folder` is where you want the data to be added in your box.

### Startup/Provision Settings <a href="startup-provision-settings" id="startup-provision-settings"></a>

When you start your box, you can install packages/run commands:

```ruby
config.vm.provision "shell", inline: <<-SHELL    
    apt-get update
    apt-get install -y apache2
SHELL
```

If you have a lot of packages to install or commands to run, you may want to put them in a separate file:

```ruby
config.vm.provision "shell", path: "install.sh"
```

### Running MacOS <a href="running-macos" id="running-macos"></a>

In order to run MacOS, you may need to reinstall.

1. Clear `csrutil` and restart.

```bash
sudo su
csrutil clear
reboot
```

2\. Uninstall from the official installer (you may have to re-download the installer if you deleted it, as the uninstall file is in there).

3\. Reinstall.

4\. Restart your computer.

5\. Install Oracle VM VirtualBox Extension Pack

6\. Install `vagrant-vbguest`:

```bash
vagrant plugin install vagrant-vbguest
```

