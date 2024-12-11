FROM postgres:latest

# Set the default PostgreSQL user and database
ENV POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=password \
    POSTGRES_DB=webstore

# Copy the custom configuration file to the container
#COPY postgresql.conf /etc/postgresql/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Set the UID and GID of the postgres user to match the host
ARG USER_ID
ARG GROUP_ID
RUN usermod -u $USER_ID postgres && groupmod -g $GROUP_ID postgres

# Set the volume mount point
VOLUME ["/var/lib/postgresql/data"]

# Start the PostgreSQL service
# CMD ["postgres"] #, "-c", "config_file=/etc/postgresql/postgresql.conf"]