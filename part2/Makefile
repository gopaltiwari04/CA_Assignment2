CXX = g++
CXXFLAGS = -O2 -static -I$(HOME)/gem5/include
M5LIB = $(HOME)/gem5/util/m5/build/x86/out/libm5.a

BENCHDIR = benchmarks

BENCHMARKS = \
	int_arithmetic \
	independent_int \
	float_compute \
	memory_access \
	mixed_compute

.PHONY: all clean run extract

all: $(BENCHMARKS:%=$(BENCHDIR)/%)

$(BENCHDIR)/int_arithmetic: $(BENCHDIR)/int_arithmetic.cpp
	$(CXX) $(CXXFLAGS) $< $(M5LIB) -o $@

$(BENCHDIR)/independent_int: $(BENCHDIR)/independent_int.cpp
	$(CXX) $(CXXFLAGS) $< $(M5LIB) -o $@

$(BENCHDIR)/float_compute: $(BENCHDIR)/float_compute.cpp
	$(CXX) $(CXXFLAGS) $< $(M5LIB) -o $@

$(BENCHDIR)/memory_access: $(BENCHDIR)/memory_access.cpp
	$(CXX) $(CXXFLAGS) $< $(M5LIB) -o $@

$(BENCHDIR)/mixed_compute: $(BENCHDIR)/mixed_compute.cpp
	$(CXX) $(CXXFLAGS) $< $(M5LIB) -o $@

extract:
	python3 extract_results.py

run:
	bash run_all.sh

clean:
	rm -f $(BENCHDIR)/int_arithmetic
	rm -f $(BENCHDIR)/independent_int
	rm -f $(BENCHDIR)/float_compute
	rm -f $(BENCHDIR)/memory_access
	rm -f $(BENCHDIR)/mixed_compute