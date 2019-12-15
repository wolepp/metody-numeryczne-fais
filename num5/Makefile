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

.PHONY: all clean release run

clean:
	rm -f *.o *.out *.csv

run:
	./$(TARGET)

release: CXXFLAGS += -o2
release: all
