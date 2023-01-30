# 没有使用cache
build_nocached:
	DOCKER_BUILDKIT=1 docker build -f Dockerfile.nocached -t demo:nocached .


build_cached:
	#DOCKER_BUILDKIT=1 docker build -f Dockerfile.cached -t demo:cached .
	buildctl --addr tcp://buildkitd.internal.gllue.com:12345 build --progress=plain  --frontend=dockerfile.v0 --local context=.  --local dockerfile=./docker --opt filename=./Dockerfile.cached --output type=image,name=registry.cn-hangzhou.aliyuncs.com/gllue/mirror:test-buildkit-slim,push=true