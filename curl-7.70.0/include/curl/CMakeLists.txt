set(CURL_SRCS
	curl.h
	curlver.h
	easy.h
	mprintf.h
	multi.h
	stdcheaders.h
	system.h
	typecheck-gcc.h
	uralpi.h
)

SET(LIB_TYPE STATIC)

add_library(curl ${LIB_TYPE} ${GEOMETRY_SRCS})