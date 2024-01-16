#!/bin/bash
npx --yes tailwindcss -i ./src/style.css -o ./static/style.css
npx --yes bun install
npx --yes bun build.js