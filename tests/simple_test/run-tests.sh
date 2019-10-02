PATH_TO_TESTS=./tests/simple_test/features
PATH_TO_TEST_ROOT=../..

cd ${PATH_TO_TEST_ROOT}

echo "### Removing old logs and screenshots"
rm -rf ./logs
rm -rf ./screenshots

echo "### Building docker image"
docker build -t dummytests -f DummyTest.dockerfile .

echo "### Running docker"
docker run --env "PATH_TO_TESTS=${PATH_TO_TESTS}" $@ dummytests
PASSED=$?

echo "### Copying logs and screenshots from container to host"
CONTAINER_ID=$(docker container list --all --last 1 --format "{{ .ID }}")
docker cp ${CONTAINER_ID}:/dummy-ui-tests/logs ./logs
docker cp ${CONTAINER_ID}:/dummy-ui-tests/screenshots ./screenshots

echo "### Finished tests"
exit ${PASSED}