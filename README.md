# 🚀 Palo Alto Networks Ansible Projects 🚀

![Palo Alto Networks Logo](images/paloaltonetworks_logo.png)

A collection of Ansible playbooks and Docker containers to automate and manage Palo Alto Networks devices.

## 📚 Table of Contents

- [🚀 Palo Alto Networks Ansible Projects 🚀](#-palo-alto-networks-ansible-projects-)
  - [📚 Table of Contents](#-table-of-contents)
  - [🌐 Project Overview](#-project-overview)
  - [🛠️ Setting Up Your Environment](#️-setting-up-your-environment)
    - [Using Invoke to Build and Access the Shell of Our Containers](#using-invoke-to-build-and-access-the-shell-of-our-containers)
    - [Creating Python Virtual Environments](#creating-python-virtual-environments)
  - [📟 Executing Standalone Ansible Projects](#-executing-standalone-ansible-projects)
    - [Using Invoke to Access the Shell of Our Containers and Executing Ansible Within the Container](#using-invoke-to-access-the-shell-of-our-containers-and-executing-ansible-within-the-container)
    - [Creating Python Virtual Environments and Executing Ansible Within the Virtual Environment](#creating-python-virtual-environments-and-executing-ansible-within-the-virtual-environment)
  - [🔬 Technical Deep Dive](#-technical-deep-dive)
    - [How the 'tasks.py' File Works with Invoke](#how-the-taskspy-file-works-with-invoke)
    - [How the Docker Containers are Built](#how-the-docker-containers-are-built)
    - [How the Various Ansible Projects Work](#how-the-various-ansible-projects-work)
  - [📖 Where to Find Documentation](#-where-to-find-documentation)
  - [🤝 Contributing](#-contributing)
  - [✍️ Author](#️-author)

## 🌐 Project Overview

This repository contains a collection of Ansible playbooks and Docker containers designed to automate and manage Palo Alto Networks devices. The project is structured with standalone Ansible playbooks residing in the "ansible" directory, each in their own subdirectory. The project root contains a `tasks.py` file which works with Invoke to manage Docker containers and run playbooks.

The container image can be built or pulled from the GitHub Container Registry. The container image is based on the official Python Docker image for both x86 and ARM CPU architectures, and includes the Palo Alto Networks Ansible collection and the required Python libraries to execute the playbooks.

## 🛠️ Setting Up Your Environment

There are two ways to set up your environment to execute the Ansible playbooks in this repository. You can either use Invoke to build the Docker containers and access the shell of the containers, or you can create Python virtual environments and execute Ansible within the virtual environments.

### Using Invoke to Build and Access the Shell of Our Containers

1. Install Invoke on your local system: `pip install invoke`
2. Run `invoke build` to build the Docker container images for all the projects in the "ansible" directory
3. Run `invoke shell` to access the shell and then navigate to a specific project's directory to execute the Ansible playbook

![Invoke Build](images/01_invoke_build.png)

### Creating Python Virtual Environments

1. Install Python virtualenv: `pip3 install virtualenv`
2. Create a virtual environment: `virtualenv venv`
3. Activate the virtual environment:
   - For Linux/Mac: `source venv/bin/activate`
   - For Windows: `venv\Scripts\activate`

## 📟 Executing Standalone Ansible Projects

### Using Invoke to Access the Shell of Our Containers and Executing Ansible Within the Container

1. Access the container shell: `invoke shell`
2. Navigate to the Ansible project directory: `cd /ansible/config_examples/<project-name>`
3. Run the Ansible playbook: `ansible-playbook <playbook-name>.yml`

![Invoke Shell](images/02_invoke_shell.png)

### Creating Python Virtual Environments and Executing Ansible Within the Virtual Environment

1. Create and activate the Python virtual environment (follow the steps in [Creating Python Virtual Environments](#creating-python-virtual-environments))
2. Install Ansible in the virtual environment: `pip install ansible`
3. Navigate to the Ansible project directory: `cd ansible/<project-type>/<project-name>`
4. Run the Ansible playbook: `ansible-playbook <playbook-name>.yml`

## 🔬 Technical Deep Dive

### How the 'tasks.py' File Works with Invoke

The `tasks.py` file is a Python script that utilizes Invoke to define tasks related to Docker container management and playbook execution. Invoke allows for command-line task execution using simple and readable commands.

### How the Docker Containers are Built

The Docker containers are built using the `Dockerfile` located in each standalone Ansible project directory. The `invoke build` command in the `tasks.py` file triggers the build process for all projects within the "ansible" directory, creating a Docker container image for each project.

### How the Various Ansible Projects Work

Each Ansible project within the "ansible" directory is designed to address a specific use case or management task for Palo Alto Networks devices. Each project consists of a playbook, roles, documentation, and any required configuration files or templates. The playbooks define the automation workflow, while roles and templates provide modularity and reusability.

## 📖 Where to Find Documentation

Project-specific documentation can be found in the README.md files within each standalone Ansible project directory. For general Ansible documentation, visit the official Ansible website: https://docs.ansible.com/

## 🤝 Contributing

We welcome contributions from the community. To contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them to your branch
4. Submit a pull request with a description of your changes

## ✍️ Author

Calvin Remsburg @cdot65
