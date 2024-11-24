set export

project_dir := justfile_directory()
AIRFLOW_HOME := project_dir / ".airflow"
AIRFLOW__CORE__DAGS_FOLDER := project_dir / "sauron_eye/dags"

airflow:
	uv run airflow standalone
