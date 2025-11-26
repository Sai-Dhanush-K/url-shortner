# URL Shortener – Technical Specification

## 1. Overview

**Goal**: Build a production-style URL shortener service with:
- Authenticated users
- Short URL generation, updation, deletion
- Redirects
- Basic analytics
- Deployed via Docker and CI/CD on a cloud platform

Primary focus is backend and DevOps. Frontend is minimal.

## 2. Functional Requirements

1. **Create Short URL**
   - Users can submit a long URL and receive a short URL.
   - Optionally set expiry date or custom code (future scope).

2. **Redirect**
   - Accessing `/{short_code}` redirects to the original URL.
   - System updates analytics on each access.

3. **User Management**
   - Email/password signup and login.
   - Authenticated users can:
     - View their URLs
     - See basic analytics (click counts, last clicked time)

4. **Analytics**
   - Store:
     - Total click count
     - Last clicked timestamp
   - Future (optional): per-day analytics, IP, country, user-agent.

## 3. Non-functional Requirements

- **Performance**: Redirect endpoint should be lightweight and fast.
- **Security**:
  - Input validation on URLs.
  - Only owners see their own URLs.
- **Scalability**: Design for horizontal scaling:
  - Stateless backend
  - Shared DB
- **Reliability**:
  - No data loss on restart.
  - Handle DB down with clear error states.
- **Observability**:
  - Logging for:
    - Short URL creations
    - Redirects
    - Errors
  - `/health` endpoint for liveness checks.

## 4. Architecture

- **Stack**:
  - Backend: Django + Django REST Framework
  - DB: PostgreSQL
  - Frontend: Basic HTML templates (Stage 1)
- **Components**:
  - API server
  - Database
  - Reverse proxy / load balancer (cloud provider or nginx later)
