.phony: docker.build docker.run docker.build.quite

run:
	@echo "Make: Running the package..."
	@python server.py

docker.build:
	@echo "Make: Building a docker image... (Might be minutes)"
	@docker build -t domain_model:dev .

docker.build.quite:
	@echo "Make: Building a docker image... (Might be minutes)"
	@docker build -q -t domain_model:dev .

docker.run: docker.build.quite
	@echo "Make: Running docker container..."
	@docker run -p 8000:8000 -v $(PWD):/app domain_model:dev run
