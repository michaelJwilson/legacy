export CONTAINER_ID=f27b96d74312

# --  August 12th 2020 --
# docker pull legacysurvey/legacypipe:DR9.6.2

# docker image ls            # Available images. 

# docker container ls --all  # List of running containers. 

# Container is an editable virtual machine.  Image is a frozen snapshot at a given time -- uneditable. 

## -d in background. 
# docker run -dit -p 8888:8888 -v /Users/MJWilson/Work/desi/legacy/docker/mjwilson:/src/mjwilson legacysurvey/legacypipe:DR9.6.2

docker exec -ti $CONTAINER_ID /bin/bash

# apt-get update && apt-get install -y emacs

# docker exec 966137c01a01 pip install jupyter

# docker exec 4a1c5d24a1e9  python legacypipe/py/legacyanalysis/model.py

# docker stop 25442f469369

##  Run in interactive mode.
##  docker container run -it -p 8888:8888 -v /Users/MJWilson/Work/desi/legacy/docker/mjwilson:/src/mjwilson legacysurvey/legacypipe:DR9.6.2 /bin/bash

##  ctrl+d to exit the session. 
