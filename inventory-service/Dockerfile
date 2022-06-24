FROM golang:1.16-alpine

WORKDIR /app/inventory-service/

COPY go.mod ./
COPY go.sum ./

RUN apk add build-base gcc

RUN go mod download
