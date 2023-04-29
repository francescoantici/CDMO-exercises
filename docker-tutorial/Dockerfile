# Pulls an image endowed with minizinc
FROM minizinc/minizinc:latest

# Setting the base folder for the container 
WORKDIR /src

# Coping all the content of this folder into the container
COPY . .  

# Installing python and its required libraries
RUN apt-get update \
  && apt-get install -y python3 \ 
  && apt-get install -y python3-pip \
  && python3 -m pip install -r requirements.txt  

# What to run when the container starts
# Use this command to keep the container up and use the terminal inside of it

CMD python3 -m http.server 

# minizinc --solver Gecode nqueens.mzn --json-stream --output-time > results/minizinc/20.json \ && python3 nqueens.py