#!/usr/bin/env bash
gunicorn app:api --bind 0.0.0.0:8200
