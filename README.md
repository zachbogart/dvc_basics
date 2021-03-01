# project_template

### Run this project with vanillin 🍦

Build image:
```
vanillin dvc_basics
```

Run JupyterLab:
```
vanillin dvc_basics 10000
```

Don't have `vanillin` installed? Add as an `oh-my-zsh` plugin [here](https://github.com/zachbogart/vanillin#vanillin)

### Run this project manually

Build image:
```
docker build --rm -t dvc_basics .
```

Run JupyterLab:
```
docker run --rm -p 10000:8888 -e JUPYTER_ENABLE_LAB=yes -v $PWD:/home/jovyan/work dvc_basics
```

Don't have Docker installed? Download [here](https://docs.docker.com/get-docker/)

