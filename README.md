# EWSN 2026 Website

Website for the EWSN 2026 Conference at TU Dresden, Germany.

## Prerequisites

- Node.js
- npm

## Build Website

The website is build using [Eleventy](https://www.11ty.dev/docs/).

### Install packages

```sh
npm install
```

### Build website

```sh
npx eleventy
```

This will build the website and output the files into the `dist/` folder.

### Start local Webserver

```sh
npx eleventy --serve
```

This will start a local webserver at `localhost:8080/`.

## Continuous Integration

[.github/workflows/build-site.yml](./.github/workflows/build-site.yml): Commits to `main` will automatically build the website and push a new commit to the `site` branch.
On the webserver, a hook can then be configure to regularly pull `site`.

For pull-requests, a preview of the website is pushed to the `preview/site` branch.

## Structure

- [`content/`](./content/): markdown files with the page content
    - **Note:** by default, all files in `content` are accessible from the frontend.
        - Prevent that a content file is accessible: set `permalink: false` in the file

- [`assets/`](./assets/): collection of styles and images that are included in the final website
    - **Note:** all files in `assets` are exposed to the frontend
- [`data`](./data/):
    - index.yml: global data
    - nav.yml: navigation data
        - the navigation path matches the folder structure in `content/`:
            - the url path of a content file is `/<folder_name>/<file_name>`
            - if `<folder_name> == <file_name>` then the path is just `/<file_name>`
        - hide path in the navbar: in `nav.yml` set `hide: true` for the item
    - accepted papers and posters YML data
    - program YML data
- [`site`](./site/):
    - [`_includes`](./site/_includes): shared template components (base, navbar, etc.)
    - [`_layouts`](./site/_layouts/): template files that are selected by content files using the `layout` property
- `dist/`: output folder for the generated website
