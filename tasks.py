"""Tasks to execute with Invoke."""

# ---------------------------------------------------------------------------
# standard library
# ---------------------------------------------------------------------------
import inspect
import os
import platform

# ---------------------------------------------------------------------------
# third party
# ---------------------------------------------------------------------------
import distro
from invoke import task


# ---------------------------------------------------------------------------
# Python3.11 hack for invoke
# ---------------------------------------------------------------------------
if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec


# ---------------------------------------------------------------------------
# Determine CPU architecture
# ---------------------------------------------------------------------------
def get_os_architecture():
    arch = platform.machine()

    if (
        "x86" in arch
        or "i386" in arch
        or "i686" in arch
        or "AMD64" in arch
        or "amd64" in arch
    ):
        return "x86"
    elif "arm" in arch or "aarch64" in arch:
        return "ARM"
    else:
        return "Unknown"


CPU_ARCHITECTURE = get_os_architecture()


# ---------------------------------------------------------------------------
# Determine Host operating system (to use Docker or Podman)
# ---------------------------------------------------------------------------
def get_container_runtime():
    dist = distro.id()

    if "rhel" in dist or "fedora" in dist or "centos" in dist:
        return "podman"
    else:
        return "docker"


CONTAINER_RUNTIME = get_container_runtime()

# ---------------------------------------------------------------------------
# CONTAINER PARAMETERS
# ---------------------------------------------------------------------------
CONTAINER_IMG = "ghcr.io/cdot65/pan-os-docker"

ARM_TAG = "arm"
X86_TAG = "x86"
VERSION = "ansible"

# ---------------------------------------------------------------------------
# SYSTEM PARAMETERS
# ---------------------------------------------------------------------------
PWD = os.getcwd()


# ---------------------------------------------------------------------------
#  CONTAINER BUILDS
# ---------------------------------------------------------------------------
@task(optional=["arm", "x86"])
def build(context, arm=None, x86=None):
    """Build our Container images."""
    if CPU_ARCHITECTURE == "x86" or x86:
        context.run(
            f"{CONTAINER_RUNTIME} build \
                -t {CONTAINER_IMG}:{X86_TAG}-{VERSION} \
                -f docker/Dockerfile \
                docker",
        )
    elif CPU_ARCHITECTURE == "ARM" or arm:
        context.run(
            f"{CONTAINER_RUNTIME} build \
                -t {CONTAINER_IMG}:{ARM_TAG}-{VERSION} \
                -f docker/Dockerfile.arm \
                docker",
        )
    else:
        context.run(
            f"{CONTAINER_RUNTIME} build \
                -t {CONTAINER_IMG}:{X86_TAG}-{VERSION} \
                -f docker/Dockerfile \
                docker",
        )


# ---------------------------------------------------------------------------
# SHELL ACCESS
# ---------------------------------------------------------------------------
@task(optional=["arm", "x86"])
def shell(context, arm=None, x86=None):
    """Get shell access to the container."""
    if CPU_ARCHITECTURE == "x86" or x86:
        context.run(
            f"{CONTAINER_RUNTIME} run -it --rm \
                -v {PWD}/docker/.zshrc:/home/ansible/.zshrc \
                -v {PWD}/ansible/playbooks:/home/ansible/playbooks \
                -w /home/ansible/playbooks \
                {CONTAINER_IMG}:{X86_TAG}-{VERSION} \
                /bin/zsh",
            pty=True,
        )
    elif CPU_ARCHITECTURE == "ARM" or arm:
        context.run(
            f"{CONTAINER_RUNTIME} run -it --rm \
                -v {PWD}/docker/.zshrc:/home/ansible/.zshrc \
                -v {PWD}/ansible/:/home/ansible/playbooks \
                -w /home/ansible/playbooks \
                {CONTAINER_IMG}:{ARM_TAG}-{VERSION} \
                /bin/zsh",
            pty=True,
        )
    else:
        context.run(
            f"{CONTAINER_RUNTIME} run -it --rm \
                -v {PWD}/ansible:/home/ansible \
                -w /home/ansible/ \
                {CONTAINER_IMG}:{X86_TAG}-{VERSION} \
                /bin/sh",
            pty=True,
        )
