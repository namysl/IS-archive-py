cmake_minimum_required(VERSION 2.8)
project(libs_z4)

include_directories(include)
file(GLOB SOURCES "src/*.cpp")

add_library(student STATIC ${SOURCES})
install(TARGETS student DESTINATION ~/Desktop/kolokwium2/zad4/lib/)
link_directories(~/Desktop/kolokwium2/zad4/lib/)

add_executable(stud_exec ${SOURCES})
install(TARGETS stud_exec DESTINATION ~/Desktop/kolokwium2/zad4/bin/)
