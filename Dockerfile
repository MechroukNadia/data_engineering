FROM ubuntu:latest
COPY . .

RUN apt-get update && apt-get install -y cron
RUN touch /var/log/cron.log
# Add the cron job command to the Dockerfile
RUN echo "* * * * * root /cron_sc.bat > /var/log/cron.log 2>&1" > /etc/cron.d/cron_job

# Run any other necessary commands for your image
COPY requirements.txt .
RUN apt-get install -y python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN crontab /etc/cron.d/cron_job

# Start cron when the container st
CMD cron && tail -f /var/log/cron.log