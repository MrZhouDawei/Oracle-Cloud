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