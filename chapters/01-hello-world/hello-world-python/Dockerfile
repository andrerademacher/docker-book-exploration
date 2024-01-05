FROM python:3.12
ENV TZ="Europe/Amsterdam"
COPY *.py *.j2 /src/
RUN python -m pip install Jinja2
USER www-data
CMD ["python", "/src/server.py"]