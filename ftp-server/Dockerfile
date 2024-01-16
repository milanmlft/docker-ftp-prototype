FROM delfer/alpine-ftp-server:latest

# FIXME: Enable SSL in FTP server configuration
RUN echo "ssl_enable=YES" >> /etc/pure-ftpd.conf
RUN echo "allow_anon_ssl=YES" >> /etc/pure-ftpd.conf
RUN echo "force_local_data_ssl=YES" >> /etc/pure-ftpd.conf
RUN echo "force_local_logins_ssl=YES" >> /etc/pure-ftpd.conf
RUN echo "ssl_sslv2=NO" >> /etc/pure-ftpd.conf
RUN echo "ssl_sslv3=NO" >> /etc/pure-ftpd.conf
RUN echo "ssl_tlsv1=YES" >> /etc/pure-ftpd.conf
RUN echo "ssl_tlsv1_1=YES" >> /etc/pure-ftpd.conf
RUN echo "ssl_tlsv1_2=YES" >> /etc/pure-ftpd.conf
RUN echo "ssl_required=YES" >> /etc/pure-ftpd.conf
RUN echo "rsa_cert_file=/etc/ssl/private/localhost.crt" >> /etc/pure-ftpd.conf
RUN echo "rsa_private_key_file=/etc/ssl/private/localhost.key" >> /etc/pure-ftpd.conf
