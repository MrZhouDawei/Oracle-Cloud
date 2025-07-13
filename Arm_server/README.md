# Minecraft Server Setup on Oracle Instance (Unix-based OS)

This guide will walk you through setting up a Minecraft server (vanilla or modded) on an Oracle Cloud instance using Docker and Docker Compose. It also includes uploading your existing world files.

## Table of Contents

1. [Set Up Oracle Cloud Instance](#set-up-oracle-cloud-instance)
2. [Generate and Configure SSH Access](#generate-and-use-ssh-keys-on-unix)
3. [Create Local Scripts](#create-connection-and-upload-scripts-on-your-local-machine)
4. [Connect and Install Dependencies](#connect-and-install-docker)
5. [Set Up Minecraft Directories](#set-up-minecraft-directories)
6. [Upload Existing World (Optional)](#upload-existing-world-optional)
7. [Start the Server](#start-the-minecraft-server)
8. [Add Additional Server](#add-additional-servers)
9. [License](#license)
10. [Contacts](#contacts)

## Set Up Oracle Cloud Instance 

Follow this tutorial until the create instance section to:

* Create an always-free compute instance
* Generate and download your SSH key
* Set up networking (VCN, Subnet, Security Rules)

Guide link: [Oracle Free Tier & Instance Set Up](https://www.reddit.com/r/admincraft/comments/qo78be/creating_a_minecraft_server_with_oracle_cloud/)

>[!TIP]\
> Check online but generally 3-4 cores and 10GB RAM should be more than enough to run any server even with mods, for a public server to find the min specs try testing on your own

## Generate and Use SSH Keys on Unix

Oracle’s guide defaults to Windows. If you're on macOS or Linux, follow this SSH guide instead:

SSH on Unix guide: [SSH Access for Oracle Instance on Unix](https://docs.oracle.com/it-it/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#linux-from-unix)

> [!IMPORTANT]\
> World folder, ssh keys and scripts are supposed to be in the same folder to make the guide easier to follow

## Create Connection and Upload Scripts (on your local machine)

> connection.sh—**SSH into the server**

```sh
#!/bin/sh

chmod 400 ssh-private-key-name.key
ssh -i ssh-private-key-name.key opc@server_ip
```
> uploads.sh-**Upload your Minecraft world folder(if you have any)**

```sh
#!/bin/sh

scp -i ssh-private-key-name.key -r "$1" opc@server_ip:~/uploads/

```
>[!TIP]\
> To run script: ./uploads.sh. /path/to/your/world

Make both scripts executable:

```sh
chmod 700 connection.sh upload.sh
```

## Connect and Install Docker **
Connect to your instance:
```sh
./connection.sh
```
Then on the remote server:
```sh
sudo dnf update
```
### Install Docker ###

[Docker on RHEL](https://docs.docker.com/engine/install/rhel/#install-using-the-repository)

### Install Docker Compose Plugin ###

[Docker Compose on RHEL](https://docs.docker.com/compose/install/linux/#install-using-the-repository)

## Set Up Minecraft Directories ##
Run the following:

```sh
mkdir minecraft uploads
cd minecraft
mkdir vanilla mod
```

Create the <span style="background-color: rgb(64,64,64)">docker-compose.yml</span> file:

```sh
nano ./vanilla/docker-compose.yml
```
Refer to this template:

Example config: [docker-compose.yml](docker-compose.yml)

## Upload Existing World (Optional) ##

From your **local machine**:

```sh
./upload.sh /path/to/your/world
```

On the server:
```sh
sudo chown -R $(whoami):$(whoami) ./vanilla
sudo chmod -R u+rw ./vanilla
cp -r ../uploads/your-uploaded-folder ./vanilla/world
```

## Start the Minecraft Server ##
```sh
sudo docker compose up -d
```
**Now you can finally find the server on the launcher using: 
publicip:port-specified-dockercomposefile!!**

## Add Additional Servers ##
To run another server:

1. Create a new folder inside minecraft (e.g., mod)
2. Add a new service block in docker-compose.yml using a different port
3. Upload a different world folder if needed
4. Repeat the volume binding and configuration

## To Do ##
- [ ] Add Backup World Service
- [ ] Add Server Route Service

## License ##

This project is distributed under the [Apache License](LICENSE)

## Contacts ##

Do you need help?:  [daweizhou2002@gmail.com](mailto:daweizhou2002@gmail.com)

