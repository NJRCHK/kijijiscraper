# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /cygdrive/c/Users/Nathaniel/.CLion2019.2/system/cygwin_cmake/bin/cmake.exe

# The command to remove a file.
RM = /cygdrive/c/Users/Nathaniel/.CLion2019.2/system/cygwin_cmake/bin/cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /cygdrive/c/kijijiscraper

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /cygdrive/c/kijijiscraper/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/kijijiscraper.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/kijijiscraper.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/kijijiscraper.dir/flags.make

CMakeFiles/kijijiscraper.dir/spider.c.o: CMakeFiles/kijijiscraper.dir/flags.make
CMakeFiles/kijijiscraper.dir/spider.c.o: ../spider.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/cygdrive/c/kijijiscraper/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/kijijiscraper.dir/spider.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/kijijiscraper.dir/spider.c.o   -c /cygdrive/c/kijijiscraper/spider.c

CMakeFiles/kijijiscraper.dir/spider.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/kijijiscraper.dir/spider.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /cygdrive/c/kijijiscraper/spider.c > CMakeFiles/kijijiscraper.dir/spider.c.i

CMakeFiles/kijijiscraper.dir/spider.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/kijijiscraper.dir/spider.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /cygdrive/c/kijijiscraper/spider.c -o CMakeFiles/kijijiscraper.dir/spider.c.s

# Object files for target kijijiscraper
kijijiscraper_OBJECTS = \
"CMakeFiles/kijijiscraper.dir/spider.c.o"

# External object files for target kijijiscraper
kijijiscraper_EXTERNAL_OBJECTS =

kijijiscraper.exe: CMakeFiles/kijijiscraper.dir/spider.c.o
kijijiscraper.exe: CMakeFiles/kijijiscraper.dir/build.make
kijijiscraper.exe: CMakeFiles/kijijiscraper.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/cygdrive/c/kijijiscraper/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable kijijiscraper.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/kijijiscraper.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/kijijiscraper.dir/build: kijijiscraper.exe

.PHONY : CMakeFiles/kijijiscraper.dir/build

CMakeFiles/kijijiscraper.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/kijijiscraper.dir/cmake_clean.cmake
.PHONY : CMakeFiles/kijijiscraper.dir/clean

CMakeFiles/kijijiscraper.dir/depend:
	cd /cygdrive/c/kijijiscraper/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /cygdrive/c/kijijiscraper /cygdrive/c/kijijiscraper /cygdrive/c/kijijiscraper/cmake-build-debug /cygdrive/c/kijijiscraper/cmake-build-debug /cygdrive/c/kijijiscraper/cmake-build-debug/CMakeFiles/kijijiscraper.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/kijijiscraper.dir/depend

