CXX 	  	:= g++
CXXFLAGS	:= -pedantic-errors -Wall -Wextra -Werror
SRC			:= $(wildcard *.cpp)
OBJECTS		:= $(SRC:%.cpp=%.o)
TARGET 		:= NUM5.out

all: $(TARGET)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c $<

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)

.PHONY: all clean clean_compile release run

clean_compile:
	rm -f *.o *.out

clean: clean_compile
	rm -f *.csv

run: release
	./$(TARGET)

release: CXXFLAGS += -o2
release: all
