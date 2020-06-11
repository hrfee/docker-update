# docker-update

A small utility I use to deploy permanent docker containers and keep them updated.

Depends on the docker python API.

`pip3 install docker`

After that, add the bin directory to your path, and make sure `definitions.py` is in the parent directory.

```
hrfee@lab /m/s/docker-update# docker-update -h
usage: docker-update [-h] [-a] [container]

positional arguments:
  container   name of the container.

optional arguments:
  -h, --help  show this help message and exit
  -a, --all   Updates all available containers
```

`definitions.py`:
```
containers = {
    "container_name": {
        "command": '',
        # Command to create container. 
        # Remove the image name from this as it goes below.'
        "repo": '',
        # Docker image name/path.
        "after": ''
        # Command to run after the creation and start of the container.
        # I use this personally to install some utilities in my homeassistant container.'
    }
}
