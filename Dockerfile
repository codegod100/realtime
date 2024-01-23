FROM cgr.dev/chainguard/wolfi-base
RUN apk update && apk add pixi posix-libc-utils
