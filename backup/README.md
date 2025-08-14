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

> [!Important] 
> Make sure you bind host paths with -v /host/path:/container/path so archives are saved on your host and not into Docker-managed anonymous volumes. See the section "If you forget to mount" below.
>
> 
### What happens if you DON'T mount `/data` or `/destination`

If you run the container without  
`-v /host/path:/data` **or**  
`-v /host/path:/destination`,  
Docker will create anonymous volumes for the `VOLUME` paths declared in the image (or mount ephemeral temporary filesystems).  
The container will still see `/data` and `/destination` as mountpoints and your backup script may run successfully — but the resulting archives will be stored inside Docker's volume store (not in a host directory you control) and can appear “lost”.

### If `/data` is empty or not mounted

 If the source directory is empty  or not mounted the backup will still run but produce an empty archive.  

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

