FROM jetpackio/devbox:latest

# Installing your devbox project
WORKDIR /home/devbox
USER ${DEVBOX_USER}:${DEVBOX_USER}
COPY --chown=${DEVBOX_USER}:${DEVBOX_USER} . .



RUN devbox run -- echo "Installed Packages."

RUN devbox shellenv --init-hook >> ~/.profile
CMD devbox run server