FROM fedora:latest

# Install dependencies and Flask
RUN dnf install -y \
    python3 \
    python3-pip \
    git \
    curl \
    htop \
    iputils \
    procps \
 && pip3 install flask \
 && dnf clean all

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Expose port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python3", "flask_static_page.py"]
