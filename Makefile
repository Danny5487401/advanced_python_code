build_nocached:
	DOCKER_BUILDKIT=1 docker build -f Dockerfile.nocached -t demo:nocached .


build_cached:
	DOCKER_BUILDKIT=1 docker build -f Dockerfile.cached -t demo:cached .