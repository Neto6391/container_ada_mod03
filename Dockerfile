# ---------------------------------
# Etapa 1: Backend Flask (Alpine)
# ---------------------------------
FROM python:3.10-alpine AS flask-build

LABEL maintainer="neto6391@gmail.com"

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

RUN pip install --no-cache-dir poetry

WORKDIR /app/backend

COPY ./backend/pyproject.toml ./backend/poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi && \
    rm -rf ~/.cache/pypoetry

COPY ./backend/ ./

# ---------------------------------
# Etapa 2: Frontend React (Alpine)
# ---------------------------------
FROM node:18-alpine AS react-build

WORKDIR /app/frontend

COPY --chown=node:node ./package*.json ./

RUN npm ci --legacy-peer-deps && \
    npm cache clean --force

COPY --chown=node:node ./ ./

RUN npm run build

# ---------------------------------
# Etapa Final: Produção com Flask e Nginx
# ---------------------------------
FROM python:3.10-alpine

RUN apk add --no-cache nginx



WORKDIR /app/backend

COPY --from=flask-build /app/backend /app/backend
COPY --from=flask-build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=flask-build /usr/local/bin /usr/local/bin

COPY --from=react-build /app/frontend/dist /usr/share/nginx/html

COPY ./devops/nginx/nginx.conf /etc/nginx/nginx.conf

ENV FLASK_APP=app/main.py
ENV FLASK_ENV=production
ENV PORT=3000

EXPOSE 3000 5173

CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=$PORT & nginx -g 'daemon off;'"]