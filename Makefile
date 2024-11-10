.PHONY: airflow

PROJECT_ROOT:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
.EXPORT_ALL_VARIABLES:
  AIRFLOW_HOME=$(PROJECT_ROOT)/.airflow
  AIRFLOW__CORE__DAGS_FOLDER=$(PROJECT_ROOT)/sauron-eye/dags

airflow:
	uv run airflow standalone


airflow/migrate:
	uv run airflow db migrate

airflow/webserver:
	uv run airflow webserver --port 8080

airflow/scheduler:
	uv run airflow scheduler
