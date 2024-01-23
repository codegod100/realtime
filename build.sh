#!/bin/bash
bun install
bun build.js
npx run -y tailwindcss -i ./src/style.css -o ./static/style.css