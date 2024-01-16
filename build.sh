#!/bin/bash
npx --yes bun install
npx --yes bun build.js
npx --yes tailwindcss -i ./src/style.css -o ./static/style.css