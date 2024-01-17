#!/bin/bash
bun install
bun build.js
tailwindcss -i ./src/style.css -o ./static/style.css