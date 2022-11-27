# The binary to build (just the basename).
MODULE := src

IMAGE := $(REGISTRY)/$(MODULE)

# This version-strategy uses git tags to set the version string
TAG := $(shell git describe --tags --always --dirty)

BLUE='\033[0;34m'
NC='\033[0m' # No Color

run:
	@python -m $(MODULE)

test:
	@pytest

lint:
	@echo "\n${BLUE}Running black against source and test files...${NC}\n"
	@black $(MODULE)
	@echo "\n${BLUE}Running Pylint against source and test files...${NC}\n"
	@pylint --rcfile=setup.cfg **/*.py
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8
	@echo "\n${BLUE}Running Bandit against source files...${NC}\n"
	@bandit -r --ini setup.cfg

grpc-gen:
	@python -m grpc_tools.protoc ./src/proto/*.proto --proto_path generated=./src/proto --python_out=./src --grpc_python_out=./src
	@sed -i -E 's/^import.*_pb2/from . \0/' ./$(MODULE)/generated/*.py

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
