FROM alpine
WORKDIR /realtime
RUN apk update && apk add bash curl git sudo shadow xz
RUN curl -fsSL https://get.jetpack.io/devbox | FORCE=1 bash
RUN sh <(curl -L https://nixos.org/nix/install) --daemon --yes
COPY  . .
RUN devbox run -- echo "Packages Installed"
CMD devbox run server
