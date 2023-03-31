<!-- vale Microsoft.HeadingAcronyms = NO -->
# convertflac: Convert FLAC CLI
<!-- vale Microsoft.HeadingAcronyms = YES -->

[![Test](https://github.com/haru52/convertflac/actions/workflows/test.yml/badge.svg)](https://github.com/haru52/convertflac/actions/workflows/test.yml)
[![Release](https://github.com/haru52/convertflac/actions/workflows/release.yml/badge.svg)](https://github.com/haru52/convertflac/actions/workflows/release.yml)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://haru52.github.io/convertflac/CODE_OF_CONDUCT.html)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://commitizen.github.io/cz-cli/)
[![semantic-release: conventionalcommits](https://img.shields.io/badge/semantic--release-conventionalcommits-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

## Overview

convertflac converts FLAC audio files into ALAC or MP3 files.

## Requirements

| Tool   | Version |
| ------ | ------- |
| FFmpeg | ^5.1.2  |

## Installation

```sh
pip install convertflac
```

## Usage

```console
Usage: convertflac [OPTIONS] INPUT_DIRECTORY_PATH
                   [OUTPUT_DIRECTORY_PATH]

  Convert FLAC audio files into Apple Lossless Audio Codec (ALAC) or
  MP3 320kbps CBR files.

Options:
  --version         Show the version and exit.
  -c, --codec TEXT  Set the output codec (alac or mp3. Default: alac).
  -h, --help        Show this message and exit.
```

If you don't input `[OUTPUT_DIRECTORY_PATH]`, convertflac makes `alac` or `mp3` directory in the current directory and sets this `alac/` or `mp3/` as the output directory.

## Update

```sh
pip install -U convertflac
```

## Uninstall

```sh
pip uninstall convertflac
```

## Description

- convertflac converts FLAC audio files into Apple Lossless Audio Codec (ALAC) or MP3 320kbps CBR files
- The output preserves the input directory structure
- The output ALAC/MP3 files preserve the input FLAC files' metadata
- If an ALAC/MP3 file with the same name already exists at the output directory, convertflac doesn't overwrite it

## Versioning policy

[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)

## License

[MIT](https://github.com/haru52/convertflac/blob/main/LICENSE)

## Contributing

[Contributing Guideline](https://haru52.github.io/convertflac/CONTRIBUTING.html)

## Documentation

[Documentation | convertflac](https://haru52.github.io/convertflac/)

<!-- vale Microsoft.Vocab = NO -->
## Author
<!-- vale Microsoft.Vocab = YES -->

[haru](https://haru52.com/)
