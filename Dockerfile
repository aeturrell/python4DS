# DOCKERFILE for Python for Data Science

# Set base image
FROM python:3.10-slim-bookworm

WORKDIR /app

# Update Linux package list and install some key libraries, including latex
RUN apt-get -y update && apt-get install -y openssl graphviz \
    nano texlive graphviz-dev \
    bash build-essential git curl

# change default shell from ash to bash
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

# Create the environment:
COPY uv.lock .
COPY pyproject.toml .

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.5.15 /uv /bin/uv

# Copy the current directory contents into the container at /app
COPY . /app

WORKDIR "/app"

# Install everything at once:
RUN uv sync

RUN uv pip list

RUN echo "Success building the Python4DS container!"
