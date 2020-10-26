#!/usr/bin/env make

.DEFAULT_GOAL := usage
COMMIT_ID :=$(shell git rev-parse HEAD)


build: ## Builds application image
	@docker build --tag rekha-app --build-arg COMMIT_ID=${COMMIT_ID} .

usage: ## Usage
	@echo '[build:  Builds application image]'