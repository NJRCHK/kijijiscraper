cmake_minimum_required(VERSION 3.15)
project(kijijiscraper C)

set(CMAKE_CXX_STANDARD 99)

add_executable(kijijiscraper spider.c)

add_library(curl-7.70 INTERFACE)
target_include_directories(curl-7.70 INTERFACE curl-7.70/ )