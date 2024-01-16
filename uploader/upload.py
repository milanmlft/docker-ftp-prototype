"""Uploads files to ftp"""
import ftplib
from ftplib import FTP_TLS
import os


def main():
    """Upload hardcoded local file to hardcoded directory in sftp server."""
    ftp = _connect_to_sftp()

    # Create the remote directory if it doesn't exist
    remote_directory = 'new-extract'
    _create_and_set_as_cwd(ftp, remote_directory)

    local_file_path = '/app/data/public.zip'
    # Store the file using a binary handler
    with open(local_file_path, 'rb') as local_file:
        output_filename = os.path.basename(local_file_path)
        command = f'STOR {output_filename}'
        print(f"running {command}")
        ftp.storbinary(command, local_file)

    # Close the FTP connection
    ftp.quit()
    print("Done!")


def _connect_to_sftp() -> FTP_TLS:
    # Set your FTP server details
    ftp_host = 'ftp-server'
    ftp_port = 21  # FTPS usually uses port 21
    ftp_user = 'prototype'
    ftp_password = 'mypass'
    # Connect to the server and login
    ftp = FTP_TLS()
    ftp.connect(ftp_host, ftp_port)
    ftp.login(ftp_user, ftp_password)
    # Switch to secure data connection
    ftp.prot_p()
    return ftp


def _create_and_set_as_cwd(ftp, project_dir) -> None:
    try:
        ftp.cwd(project_dir)
        print(f"'{project_dir}' exists on remote ftp, so moving into it")
    except ftplib.error_perm:
        print(f"creating '{project_dir}' on remote ftp and moving into it")
        # Directory doesn't exist, so create it
        ftp.mkd(project_dir)
        ftp.cwd(project_dir)


if __name__ == "__main__":
    main()
