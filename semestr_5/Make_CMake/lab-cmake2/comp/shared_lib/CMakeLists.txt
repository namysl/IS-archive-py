cmake_minimum_required(VERSION 2.6)
project(shared_lib)
include_directories(include)
set(SOURCES src/Student.cpp ../lib_comp/src/mainapp.cpp)
add_executable(student ${SOURCES})

