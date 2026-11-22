// @ts-check
import { defineConfig } from 'astro/config';

// Wersja podglądowa: niepubliczna (noindex + robots Disallow).
export default defineConfig({
  site: process.env.SITE_URL ?? 'https://sherocky.band',
  base: process.env.BASE_PATH ?? '/',
  trailingSlash: 'ignore',
  build: { format: 'directory' },
});
