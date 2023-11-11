FROM debian:bookworm-slim
RUN apt update && apt install -y curl
WORKDIR /workspace/realtime
RUN curl -fsSL https://pixi.sh/install.sh | bash
ENV PIXI /root/.pixi/bin/pixi
COPY . .
RUN ${PIXI} run dep_install
CMD ${PIXI} run dev