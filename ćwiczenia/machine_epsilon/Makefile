CXX 	  	:= g++
CXXFLAGS	:= -pedantic-errors -Wall -Wextra -Werror
SRC			:= $(wildcard *.cpp)
OBJECTS		:= $(SRC:%.cpp=%.o)
TARGET 		:= machine_epsilon.x

all: $(TARGET)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c $<

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)

.PHONY: all clean release

clean:
	rm -f *.o *.x

release: CXXFLAGS += -o2
release: all
