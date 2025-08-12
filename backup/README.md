#  Backup Tool

A lightweight container that compresses a mounted source directory into a timestamped archive (zip, tar, gztar, bztar, xztar).  
Ideal for simple, cron-style backups inside CI pipelines, IoT devices, or on any Docker-compatible host.

##  Quick Start
 
  ```bash
    docker run --rm \
     -e backup_type=gztar \
     -e backup_name=project_backup_ \
     -v /host/data:/data \
     -v /host/backups:/destination \
     daweizhou22/python-backup-script
  ```

## More Info

Check the Docker Hub image for more information: [python-backup-script](https://hub.docker.com/r/daweizhou22/python-backup-script)


##  Multiple Copies on Cloud

You can store multiple backup copies in the cloud using: **rclone**

### Quick Steps

[Install](https://rclone.org/install/)\
[Download rclone for setup](https://rclone.org/downloads/)\
[Setup Config file](https://rclone.org)
> [!IMPORTANT]
> Every Cloud Provider has a different Configuration Steps

### How to use

[Rclone Manual](https://rclone.org/commands)
- Using Host:
  ```bash
    rclone command source:path/to/file destination:path/to/Cloudfile
  ```
- Using Docker Image:
  ```bash
    docker run --rm \
      --volume ~/config/rclone:/config/rclone \
      --volume ~/my_backups:/data \
      rclone/rclone \
      rclone command source:path dest:path
  ```


## Credits

[Rclone Official Webpage](https://rclone.org)\
\
[Rclone Docker Image Guide](https://samjenkins.com/rclone-docker-setup/#steps-to-set-up-rclone-docker-image)

