# project_template

### Run this project with vanillin 🍦

Build image:
```
vanillin DOCKER_IMAGE_NAME
```

Run JupyterLab:
```
vanillin DOCKER_IMAGE_NAME 10000
```

Don't have `vanillin` installed? Add as an `oh-my-zsh` plugin [here](https://github.com/zachbogart/vanillin#vanillin)

### Run this project manually

Build image:
```
docker build --rm -t DOCKER_IMAGE_NAME .
```

Run JupyterLab:
```
docker run --rm -p 10000:8888 -e JUPYTER_ENABLE_LAB=yes -v $PWD:/home/jovyan/work name
```

Don't have Docker installed? Download [here](https://docs.docker.com/get-docker/)

***

# Vanillin

Get coding using community Jupyter containers ("regular cola", 😀) just the way you like 'em ("vanilla cola", 🤩).

**A plugin for oh-my-zsh** and **A repo template**: makes it easier to work with Jupyter Docker containers, simplifying commands and providing a simple project template.

## Add vanillin oh-my-zsh plugin

Using [oh-my-zsh](https://ohmyz.sh/), add vanillin as a plugin. Makes it easier to build/run project docker containers for JupyterLab.

- Follow along below
- Or here's a direct link to the [`vanillin.plugin.zsh` file](https://gist.githubusercontent.com/zachbogart/c01e88886855c39c4058d0baa43ec9ec)

### Plugin Walkthrough

Run this code in Terminal:
```
mkdir $ZSH_CUSTOM/plugins/vanillin
wget -O $ZSH_CUSTOM/plugins/vanillin/vanillin.plugin.zsh https://gist.githubusercontent.com/zachbogart/c01e88886855c39c4058d0baa43ec9ec/raw/vanillin.plugin.zsh
```

Open `~/.zshrc` and add vanillin as a plugin. With comments, probably looks something like:
```
# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git vanillin)
```

Update:
```
source ~/.zshrc
```

- Uses [this Gist](https://gist.github.com/zachbogart/c01e88886855c39c4058d0baa43ec9ec) to create vanillin alias

### Usage

```
🍦  -- Example --
🍦
🍦    Build `cool_image_name` from pwd Dockerfile
🍦     and run JupyterLab on the result, on port 10000
🍦
🍦    1. `vanillin cool_image_name`
🍦    2. `vanillin cool_image_name 10000`
```

Type `vanillin` for usage:
```
🍦
🍦 Vanillin: alias for docker build/run JupyterLab commands
🍦 - GitHub: https://github.com/zachbogart/vanillin
🍦
🍦 Usage:
🍦
🍦  vanillin name
🍦    Alias for: `docker build --rm -t name .`
🍦    - Shorthand for building image from pwd Dockerfile
🍦
🍦  vanillin name port
🍦    Alias for: `docker run --rm -p port:8888 -e JUPYTER_ENABLE_LAB=yes -v $PWD:/home/jovyan/work name`
🍦    - Shorthand for running JupyterLab
🍦
🍦  -- Example --
🍦
🍦    Build `cool_image_name` from pwd Dockerfile
🍦     and run JupyterLab on the result, on port 10000
🍦
🍦    1. `vanillin cool_image_name`
🍦    2. `vanillin cool_image_name 10000`
🍦
```

## Use this repo as a template

Can use this repo as a template for a new project. Simply:

1. Rename/Find & Replace `DOCKER_IMAGE_NAME` at the top to specify how you want to title your local images for this project
2. Remove Doc info from this README (info after first line break)
3. Ready to Go!

*** 

### What is this?

**A template** for making projects that use Jupyter Docker Images to run JupyterLab and **an alias for zsh** to make it easier to build/run the images.

Process
- Template has Dockerfile, builds off of [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) base images, adding anything specified for custom build
- Run new image, accessing [JupyterLab](https://jupyterlab.readthedocs.io/)
- Includes nice alias function to avoid having to type really long docker commands

### Why?

- Depend on Docker: Much less hassle regarding dependencies. Just specify a base image and go
- Easy to customize: add a `pip install` or `install.packages` to Dockerfile as `RUN` commands, and can tailor image to project-specific needs
- Easy to share: Dockerfile describes dependencies, can run/work in same environment
- R and Python at once: Go back and forth between R/Python in same Jupyter Environment with something like [jupyter-datascience-notebook](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook)

### What the `docker run` Command Does

This command is explained in the [Jupyter Docker Stacks Quickstart](https://jupyter-docker-stacks.readthedocs.io/en/latest/#quick-start), Example 3

### Caveats

- Installs using Jupyter Community Docker images can be large (2-4 GB). First install may take a few minutes, but using the same base image across different projects will reduce any instances of large install wait times (Docker will use cached base image). So don't get scared downloading a big base image: reuse it and every project afterwards will be speedy to build.

### Further Reading

- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/): Main documentation for "ready-to-run Docker images containing Jupyter applications and interactive computing tools". This explains all the ins-and-outs regarding the image setup, versioning schema, setting up additional features, etc.
- [Image Selection](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html): All docker images from Jupyter available on DockerHub, used as starting point for this repo. Can easily find image by filtering for given type, links to DockerHub.

***

Made with 💖
