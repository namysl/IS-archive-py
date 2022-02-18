cmake_minimum_required(VERSION 2.6)
project(LIB_COMP)
include_directories(include)
set(SOURCES src/mainapp.cpp src/Student.cpp)
add_executable(student ${SOURCES})

