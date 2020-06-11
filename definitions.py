containers = {
    "jf-accounts": {
        "command": 'docker create --name jf-accounts --restart always -v /etc/localtime:/etc/localtime:ro -p 8056:8056 -v /media/docker/jf-accounts:/data -v /media/docker/jellyfin:/jf',
        "repo": "hrfee/jellyfin-accounts:latest"
    }
}
