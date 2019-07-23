#!/usr/bin/env python3
# -*- compile-command: "./kumodd.py -c config/test.yml -s gdrive -l pdf"; -*-
__author__ = 'andrsebr@gmail.com (Andres Barreto), rich.murphey@gmail.com'

# Copyright (C) 2019  Andres Barreto and Rich Murphey

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from absl import app, flags
import logging
import modules.gdrive as gdrive
import os
import platform
import sys 

kumodd_verison = "1.0.1"

FLAGS = flags.FLAGS

flags.DEFINE_enum('log', 'ERROR',
                  ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                  'Set the level of logging detail.')
flags.DEFINE_enum('service', 'gdrive',
                  ['gdrive','dropbox','box','onedrive'], 'Service to use', short_name='s' )
flags.DEFINE_enum('list', None,
                  ['all', 'doc', 'xls', 'ppt', 'text', 'pdf', 'office', 'image', 'audio', 'video', 'other'],
                  'List files in google drive and verify files on disk match MD5', short_name='l')
flags.DEFINE_enum('download', None,
                  ['all', 'doc', 'xls', 'ppt', 'text', 'pdf', 'office', 'image', 'audio', 'video', 'other'],
                  'Download files, optionally filter, and verify MD5 on disk', short_name='d')
flags.DEFINE_list('usecsv', None,
                  'List files in cloud,  files, optionally filter, and verify MD5 of files on disk', short_name='csv')
flags.DEFINE_string('destination', './download', 'Destination folder location', short_name='p')
flags.DEFINE_string('metadata_destination', './download/metadata',
                    'Destination folder for metadata information', short_name='m')
flags.DEFINE_boolean('version', False, 'Print version number and exit.')

def main(argv):
    try:
        argv = FLAGS(argv)
    except flags.FlagsError as e:
        print( f"Error: {e}" )
        print( f"\nUsage: {argv[0]} ARGS\n\n{FLAGS}" )
        sys.exit(1)
        
    if platform.system() == 'Windows':
        import wmi
        cwmi = wmi.WMI()
        pid = os.getpid()
        for x in range(3):
            for process in cwmi.Win32_Process(ProcessId=pid):
                pid = process.ParentProcessId
                if 'explorer' in process.name.lower():
                    print(f"""
Kumodd is a command line utility.
Please execute it from a cmd shell or powershell.

Usage: {argv[0]} [ARGS...]

{FLAGS}

press any key to exit.
""")
                    sys.stdin.read(1)
                    sys.exit(1)

    if FLAGS.version:
        print('version: ', kumodd_verison )
        sys.exit(1)

    if not os.path.exists(FLAGS.destination):
        os.makedirs(FLAGS.destination)
            
    if FLAGS.service == 'gdrive':
        flags.DEFINE_string('logfile', 'gdrive.log', 'Location of file to write the log' )
        gdrive.main(argv)
    elif FLAGS.service == 'dropbox':
        print( 'Coming soon...' )
    elif FLAGS.service == 'box':
        print( 'Coming soon...' )
    elif FLAGS.service == 'onedrive':
        print( 'Coming soon...' )
    
if __name__ == '__main__':
    app.run(main)


