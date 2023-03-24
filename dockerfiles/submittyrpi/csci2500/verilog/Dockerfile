FROM debian:stretch-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
    && rm -rf "/var/lib/apt/lists/*"

RUN apt-get update \
    && apt-get install -y iverilog gtkwave \
    && rm -rf "/var/lib/apt/lists/*"

# test file
RUN printf 'module main;\ninitial\nbegin\n$display("hello world");\n$finish;\nend\nendmodule\n' > /hello.v
# module main;
# initial
# begin
# $display("hello world");
# $finish;
# end
# endmodule

CMD ["/bin/bash"]

# commands to run
# in the directory of this docker file:
#   docker build .
#   docker run -it --rm sha256:<hash> /bin/bash
# in the container:
#   iverilog hello.v
#   ./a.out
