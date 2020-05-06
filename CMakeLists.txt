cmake_minimum_required(VERSION 3.15)
project(kijijiscraper C)

set(CMAKE_C_STANDARD 99)

include_directories(curl)

add_executable(kijijiscraper spider.c
        curl/curl.h
        )