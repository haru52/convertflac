import glob
import os
import subprocess
import sys

import click

from .version_getter import VersionGetter

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
DEFAULT_OUT_DIR_NAME = 'mp3'
INPUT_DIRECTORY_PATH = 'input_directory_path'
OUTPUT_DIRECTORY_PATH = 'output_directory_path'


def validate_path_is_existing_dir(arg_name, path):
    if not os.path.exists(path):
        raise click.BadParameter(
            f"{arg_name} doesn't exist:\n{path}"
        )
    if not os.path.isdir(path):
        raise click.BadParameter(
            f"{arg_name} isn't a directory:\n{path}"
        )


def is_same_path(path1, path2):
    return os.path.abspath(path1) == os.path.abspath(path2)


def escape(string):
    return string.translate(string.maketrans({'[': '[[]', ']': '[]]'}))


def encode(in_dir_path, out_root_dir_path):
    for f in glob.glob(os.path.join(escape(in_dir_path), '*')):
        if os.path.basename(f) == DEFAULT_OUT_DIR_NAME:
            continue
        if os.path.isdir(f):
            out_dir_path = os.path.join(out_root_dir_path, os.path.basename(f))
            if not os.path.exists(out_dir_path):
                os.mkdir(out_dir_path)
            encode(f, out_dir_path)

    for in_path in glob.glob(os.path.join(escape(in_dir_path), '*.flac')):
        in_basename = os.path.splitext(os.path.basename(in_path))[0]
        out_path = os.path.join(out_root_dir_path, in_basename + '.m4a')
        ffmpeg_argv = [
            'ffmpeg',
            '-i',
            in_path,
            '-ab',
            '320k',
            # Use `-codec:v copy` to preserve the album artwork
            # https://stackoverflow.com/questions/74957184/ffmpeg-converting-flac-to-mp3-changes-front-cover-image-format-and-size
            '-codec:v',
            'copy',
            '-n',
            out_path]
        try:
            print('\nEncoding ' + in_path + '\n')
            subprocess.run(ffmpeg_argv)
        except Exception as e:
            print(e, file=sys.stderr)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VersionGetter.run(), prog_name='convertflac')
@click.argument(INPUT_DIRECTORY_PATH)
@click.argument(OUTPUT_DIRECTORY_PATH, default=os.getcwd())
def main(input_directory_path, output_directory_path):
    """Convert FLAC audio files into MP3 320kbps CBR files."""

    for arg_name, path in [
        (INPUT_DIRECTORY_PATH.upper(), input_directory_path),
        (OUTPUT_DIRECTORY_PATH.upper(), output_directory_path),
    ]:
        validate_path_is_existing_dir(arg_name, path)

    in_basename = os.path.basename(input_directory_path)
    raw_out_dir_path = os.path.join(output_directory_path, in_basename)
    out_dir_path = (
        os.path.join(output_directory_path, DEFAULT_OUT_DIR_NAME, in_basename)
        if is_same_path(input_directory_path, raw_out_dir_path)
        else raw_out_dir_path)
    if not os.path.exists(out_dir_path):
        os.makedirs(out_dir_path)

    encode(input_directory_path, out_dir_path)


if __name__ == '__main__':
    main()
