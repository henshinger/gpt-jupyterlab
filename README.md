# gpt_jupyterlab

[![Github Actions Status](https://github.com/henshinger/gpt-jupyterlab/workflows/Build/badge.svg)](https://github.com/henshinger/gpt-jupyterlab/actions/workflows/build.yml)
A JupyterLab extension.

GPT JupterLab is a JupyterLab extension to use OpenAI’s GPT models(including Codex model for code completion) on your notebook cells.

This extension passes your current notebook cell to the GPT API and completes your code/text for you. You can customize the GPT parameters in the Advanced Settings menu.

This extension is composed of a Python package named `gpt_jupyterlab`
for the server extension and a NPM package named `gpt_jupyterlab`
for the frontend extension.

**Note: You will need your own OpenAI API Key to use this extension(See: [How to get OpenAI API Key](#https://www.youtube.com/watch?v=_vEJ07K0VPs))**

https://user-images.githubusercontent.com/1387307/213931801-0fdefd9d-4edd-4007-8c00-951d4ffb12b4.mp4

## Install

To install the extension, execute:

```bash
pip install gpt_jupyterlab
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall gpt_jupyterlab
```

## Getting Started

There are three ways to prompt the GPT API.

**1. Use the GPT Button in the Toolbar**

![GPT Button Screenshot](https://user-images.githubusercontent.com/1387307/213923948-863b7e28-f956-4c8c-b27b-959551952b39.png)

**2. Click `GPT Completion` under the `Edit` Menu**
![GPT Menu Screenshot](https://user-images.githubusercontent.com/1387307/213923950-bacaf820-ecb2-4220-984f-cd2b8bd69ce5.png)

**3. Use the `Ctrl`+`Space`(Windows)/`Cmd`+`Space`(Mac) Keyboard Shortcut**
![GPT Menu Screenshot](https://user-images.githubusercontent.com/1387307/213923950-bacaf820-ecb2-4220-984f-cd2b8bd69ce5.png)

## How to Change Your Settings

**Go to the `Settings` Menu and click `Advanced Settings Editor`**
![Advanced Settings Editor](https://user-images.githubusercontent.com/1387307/213924568-76b150f5-9def-427b-8a89-22ef357758ff.png)

**Click `gpt_jupyterlab` in the left sidebar**
![GPT JupyterLab Settings](https://user-images.githubusercontent.com/1387307/213924690-2df6cb67-1197-433f-afe7-42af3474767d.png)

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

If the server extension is installed and enabled, but you are not seeing
the frontend extension, check the frontend extension is installed:

```bash
jupyter labextension list
```

## Contributing

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Change directory to the gpt_jupyterlab directory
# Install package in development mode
pip install -e ".[test]"
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Server extension must be manually installed in develop mode
jupyter server extension enable gpt_jupyterlab
# Rebuild extension Typescript source after making changes
jlpm build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### Development uninstall

```bash
# Server extension must be manually disabled in develop mode
jupyter server extension disable gpt_jupyterlab
pip uninstall gpt_jupyterlab
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `gpt_jupyterlab` within that folder.

### Testing the extension

#### Server tests

This extension is using [Pytest](https://docs.pytest.org/) for Python code testing.

Install test dependencies (needed only once):

```sh
pip install -e ".[test]"
# Each time you install the Python package, you need to restore the front-end extension link
jupyter labextension develop . --overwrite
```

To execute them, run:

```sh
pytest -vv -r ap --cov gpt_jupyterlab
```

#### Frontend tests

This extension is using [Jest](https://jestjs.io/) for JavaScript code testing.

To execute them, execute:

```sh
jlpm
jlpm test
```

#### Integration tests

This extension uses [Playwright](https://playwright.dev/docs/intro) for the integration tests (aka user level tests).
More precisely, the JupyterLab helper [Galata](https://github.com/jupyterlab/jupyterlab/tree/master/galata) is used to handle testing the extension in JupyterLab.

More information are provided within the [ui-tests](./ui-tests/README.md) README.

### Packaging the extension

See [RELEASE](RELEASE.md)
