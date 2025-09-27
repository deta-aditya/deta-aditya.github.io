// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  outDir: './dist',
  site: 'https://deta-aditya.github.io',
  base: '/',
  vite: {
    plugins: [tailwindcss()]
  }
});
