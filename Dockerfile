# ============================================================
# Stage 1: Install dependencies
# ============================================================
FROM node:22-slim AS deps
WORKDIR /usr/src/app
COPY package.json package-lock.json* ./
RUN npm ci --prefer-offline

# ============================================================
# Stage 2: Runtime — build & serve Quartz
# ============================================================
FROM node:22-slim AS runner
WORKDIR /usr/src/app

# Copy node_modules from deps stage
COPY --from=deps /usr/src/app/node_modules ./node_modules

# Copy toàn bộ source (content/ sẽ được mount qua volume lúc runtime)
COPY . .

# Port mà Quartz dev-server lắng nghe
EXPOSE 8080

# Build tĩnh trước, sau đó serve — thích hợp cho production
CMD ["sh", "-c", "npx quartz build && npx quartz build --serve --port 8080"]
