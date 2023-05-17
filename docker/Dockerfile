FROM python:3.11-slim

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
LABEL name="ghcr.io/cdot65/pan-ansible-examples:x86" \
    maintainer="cremsburg.dev@gmail.com" \
    description="Docker container for PAN-OS and Panorama" \
    license="Apache 2.0" \
    url="https://github.com/cdot65/pan-ansible-examples" \
    build-date="20230406"

# ---------------------------------------------------------------------------
# Install dependencies
# ---------------------------------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        sudo \
        git \
        curl \
        vim \
        less \
        zsh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------------------------
# Create user
# ---------------------------------------------------------------------------
RUN useradd -m ansible && \
    echo "ansible ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers

# ---------------------------------------------------------------------------
# Switch to ansible user
# ---------------------------------------------------------------------------
USER ansible

# ---------------------------------------------------------------------------
# Set up Zsh shell
# ---------------------------------------------------------------------------
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
SHELL ["/bin/zsh", "-c"]

# ---------------------------------------------------------------------------
# Install Poetry
# ---------------------------------------------------------------------------
RUN curl -sSL https://install.python-poetry.org | python3 -

# ---------------------------------------------------------------------------
# Change directory to /home/ansible
# ---------------------------------------------------------------------------
WORKDIR /home/ansible
COPY pyproject.toml pyproject.toml

# ---------------------------------------------------------------------------
# Setup user's environment
# ---------------------------------------------------------------------------
ENV POETRY_VIRTUALENVS_PATH="/home/ansible/venv"
ENV ANSIBLE_CONFIG /home/ansible/ansible.cfg

# ---------------------------------------------------------------------------
# Install packages and Ansible Galaxy collections
# ---------------------------------------------------------------------------
RUN echo 'export PATH="/home/ansible/.local/bin:$PATH"' >>~/.zshrc && \
    source ~/.zshrc && \
    poetry install && \
    poetry run ansible-galaxy collection install paloaltonetworks.panos && \
    echo 'source $POETRY_VIRTUALENVS_PATH/pan-ansible-examples-*/bin/activate' >>~/.zshrc
