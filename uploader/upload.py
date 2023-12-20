"""Uploads files to ftp"""
import ftplib
from ftplib import FTP_TLS
import os


def _create_and_set_as_cwd(ftp, directory):
    print(f"creating '{directory}' on remote ftp")
    try:
        ftp.cwd(directory)
    except ftplib.error_perm:
        # Directory doesn't exist, so create it
        ftp.mkd(directory)
        ftp.cwd(directory)


def main():
    # Set your FTP server details
    ftp_host = 'ftp-server'
    ftp_port = 21  # FTPS usually uses port 21
    ftp_user = 'prototype'
    ftp_password = 'mypass'
    remote_directory = 'new-extract'

    # Local file to be uploaded
    local_file_path = '/app/data/public.zip'

    # Connect to the server and login
    ftp = FTP_TLS()
    ftp.connect(ftp_host, ftp_port)
    ftp.login(ftp_user, ftp_password)

    # Create the remote directory if it doesn't exist
    _create_and_set_as_cwd(ftp, remote_directory)

    # Store the file using a binary handler
    with open(local_file_path, 'rb') as local_file:
        output_filename = os.path.basename(local_file_path)
        command = f'STOR {output_filename}'
        print(f"running {command}")
        ftp.storbinary(command, local_file)

    # Close the FTP connection
    ftp.quit()


if __name__ == "__main__":
    main()
