#
# This file is part of Liri.
#
# Copyright (C) 2017 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com>
#
# $BEGIN_LICENSE:GPL3+$
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# $END_LICENSE$
#

import sys
import subprocess


class colors:
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUE = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAILURE = '\033[91m'
    ENDCOLOR = '\033[0m'


def message(msg):
    print('{}=={} {}{}'.format(colors.BLUE, colors.ENDCOLOR + colors.BOLD, msg, colors.ENDCOLOR))


def command(cmd, echo=False, output=False):
    """
    Execute a command and return the output.
    :param cmd: List of command parameters.
    :return: Output.
    """
    if echo:
        message('Executing: {}'.format(' '.join(cmd)))
    out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=sys.stdout.buffer).stdout
    if output:
        print(out.decode('utf-8').strip())
    return out


def prepare(src_filename, dst_filename, metadata):
    """
    Rewrite `src_filename` expanding parameters and writing `dst_filename`.
    :param src_filename: Path to the source file.
    :param dst_filename: Path to the destination file.
    :param metadata: Dictionary with app name and version.
    :return: Path to the new file.
    """
    import tempfile
    with open(src_filename, 'r') as f:
        dst = open(dst_filename, 'w')
        for line in f:
            s = line.replace(r'@@APP_BRANCH@@', metadata['version']).replace(r'@@GIT_TAG@@', metadata['tag']).replace(r'@@LIRI_SDK_VERSION@@', metadata['sdk-version'])
            dst.write(s)
        dst.close()
