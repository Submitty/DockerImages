# First Stage: Builder
FROM debian:buster-slim AS builder

# Install necessary dependencies for building GHC
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl build-essential libffi-dev libgmp-dev libtinfo5 ca-certificates xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Install GHCup (Haskell toolchain manager) without automatically installing the latest GHC
RUN curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | bash -s -- -y --no-ghc \
    && /root/.ghcup/bin/ghcup install ghc 8.10.7 \
    && /root/.ghcup/bin/ghcup set ghc 8.10.7 \
    && rm -rf /root/.ghcup/ghc/9.4.8

# Clean up unnecessary build artifacts and cache
RUN rm -rf /root/.ghcup/cache /var/lib/apt/lists/*


# Second Stage: Final Image
FROM debian:buster-slim

# Install runtime dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libffi6 libgmp10 libtinfo5 build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy GHC from the builder stage
COPY --from=builder /root/.ghcup /root/.ghcup

# Set PATH to include GHCup
ENV PATH="/root/.ghcup/bin:${PATH}"

# Set the working directory
WORKDIR /usr/src/app

# Install libgmp-dev explicitly for runtime linking
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgmp-dev \
    && rm -rf /var/lib/apt/lists/*

# Default command to keep the container running
CMD ["/bin/bash"]
