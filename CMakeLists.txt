cmake_minimum_required(VERSION 3.15)
project(kijijiscraper C)

set(CMAKE_C_STANDARD 99)

set(libcurl_INCLUDE_DIR "M:/clibs/curl-7.70.0/include")

include_directories(${libcurl_INCLUDE_DIR})
add_executable(kijijiscraper spider.c)


target_link_libraries(kijijiscraper M:/clibs/curl-7.70.0/lib/libcurl.dll.a)