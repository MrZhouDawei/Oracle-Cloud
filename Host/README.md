# Personal Hosting Platform

Containerized, secure personal services stack on Oracle Cloud using Docker, Nginx, and Cloudflare Origin TLS.

## Objectives

[:x:] file server\
[ ] web server\
[ ] email server\
[ ] password manager\
[ ] media player\
[ ] storage service + auto back-up

## Overview

This project provides a framework to self‑host multiple services behind a secure reverse proxy. It uses:

* Cloudflare Origin TLS to encrypt traffic between Cloudflare Edge and your origin server.

* Nginx in a Docker container to terminate TLS and proxy requests.

* Docker Compose to orchestrate all services within an isolated network.

* Oracle Cloud VM as the hosting environment.

Desired goal: Expand effortlessly to add web, email, and other personal services.


## File Server

### Architecture

> Browser ⇄ Cloudflare Edge ⇄ Nginx (Docker) ⇄ Filebrowser (Docker)

### Prerequisites

- Oracle Cloud VM (public IP)  
- Docker & Docker Compose installed  
- Cloudflare account + domain  
- Origin certificate  (Cloudflare offers this solution)
- Basic familiarity with Linux CLI and Docker

>**Why Origin Certificates?**\
Cloudflare encrypts traffic between the user and its edge servers. Origin Certificates ensure TLS remains encrypted end‑to‑end from Cloudflare → Nginx. 

### Repository layout

```text
/host
├── certs/                 # Cloudflare Origin certs (origin.pem, origin-key.pem)
├── files/                 # Filebrowser data & config
│   ├── data/              # user files
│   ├── database/          # filebrowser.db(users, perms, etc.)
│   └── config/            # settings.json
├── nginx/
│   └── nginx.conf         # Nginx reverse‑proxy config
└── docker-compose.yml     # Compose stack definition

```

### Getting Started

1. **Clone the repository**

```code
git clone git@github.com:MrZhouDawei/Oracle-Cloud.git
cd host
```

2.  **Add Origin Certificates**

```code
Copy origin.pem and origin-key.pem into certs/.
```

>[!TIP]\
Follow this guide if you have have as a host [Cloudflare](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/).

3. **Configure your domain**

```text
Edit nginx/nginx.conf, set server_name files.example.com with your own *.domain
```

4. **Launch the stack**

```code
docker-compose up -d
```

5. **Verify**

```code
# Locally (bypass Cloudflare edge)
curl -k --resolve owndomain:443:127.0.0.1 https://owndomain
# In browser
https://owndomain
```


### Common Task

* **View logs**

```code
docker-compose logs -f proxy fileserver
or
docker-compose logs idcontainer
```

* **Restart services**

```code
docker compose down  && docker-compose up -d
```

### License

This projoct is under [License](../Host/LICENSE).

### Contacts

Email: [daweizhou2002@gmail.com](mailto:daweizhou2002@gmail.com).

