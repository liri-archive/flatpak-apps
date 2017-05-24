Liri apps for Flatpak
=====

Recipes to build Liri apps for Flatpak.

## Build

Type the following command to build, export the repository and sign the commit with GPG:

```sh
./build --export
```

If you want to perform only a build and use the `repo` locally:

```sh
./build
```

## Versioning

Nightly builds result in the `master` OSTree branch while stable builds are in the `stable` branch.
