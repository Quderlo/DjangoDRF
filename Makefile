db-start:
	docker compose up -d postgres

db-drop:
	docker compose rm -sf postgres
	docker volume rm -f test_api_data

clean-up:
	docker system prune
	docker volume prune
	docker volume rm $(docker volume ls -qf dangling=true)

migrate:
	venv/bin/python3 src/manage.py makemigrations users
	venv/bin/python3 src/manage.py migrate