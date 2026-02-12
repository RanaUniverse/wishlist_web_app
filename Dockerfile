# ./DockerFile is this file
# Below two line i got from the uv official docs

FROM python:3.12-slim-trixie


COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


WORKDIR /app


COPY . .


RUN uv sync


EXPOSE 5000


CMD ["uv", "run", "main.py"]
