
cmake_minimum_required(VERSION 3.15)
project(kijijiscraper)
set(CMAKE_C_COMPILER c)
set(CMAKE_CXX_STANDARD 11)

add_library(curl-7.70 INTERFACE)

add_executable(kijijiscraper spider.c)

target_include_directories(curl-7.70 INTERFACE curl-7.70/ )
