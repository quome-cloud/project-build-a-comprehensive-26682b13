# Developer Setup Guide - project-build-a-comprehensive

This guide outlines the setup process for developers working on the "project-build-a-comprehensive" emergency management system.

## Prerequisites

* **Required Software Versions:**
    * **Python:** 3.9+ (for backend)
    * **Node.js:** 16+ (for frontend)
    * **Docker:** 20.10+ (Recommended for Option 1)
    * **Docker Compose:** 1.29+ (Recommended for Option 1)
    * **PostgreSQL:** 13+ (or your preferred database; adjust configurations accordingly)

* **Development Tools:**
    * Git
    * Text editor or IDE (see recommendations below)

* **IDE Recommendations and Configurations:**
    * **VS Code:** Highly recommended. Install extensions for Python, JavaScript, and PostgreSQL support.  Configure linters (e.g., Pylint for Python, ESLint for JavaScript) according to the project's `.eslintrc` and `pylintrc` files.
    * **PyCharm:** A robust IDE for Python development.  Integrates well with databases and version control.
    * **WebStorm:**  A powerful IDE for JavaScript development, good for frontend work.


## Local Development Setup

### Option 1: Docker Development (Recommended)

This option simplifies setup by encapsulating all dependencies within Docker containers.

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd project-build-a-comprehensive
   ```

2. **Docker Setup:** Ensure Docker and Docker Compose are installed and running.

3. **Development `docker-compose.yml` Configuration:**  (Example - Adjust based on your project's structure)

```yaml
version: "3.9"
services:
  web:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
      - db

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/ems_db
      - SECRET_KEY=your_secret_key  # Replace with a strong secret key
    depends_on:
      - db

  db:
    image: postgres:13
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=ems_db


```

4. **Hot Reload Setup:**  For the frontend, use a tool like `nodemon` (if not already included in your `package.json`).  For the backend, consider using a development server with automatic reloading (e.g., `uvicorn` with appropriate settings if using FastAPI).

5. **Build and Run:**
   ```bash
   docker-compose up -d --build
   ```


### Option 2: Native Development

This option requires installing dependencies directly on your system.

1. **Backend Setup (Python):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. **Frontend Setup (Node.js):**
   ```bash
   cd frontend
   npm install
   ```

3. **Database Setup:** Install PostgreSQL. Create a database named `ems_db` (or as specified in your configuration) with a user named `postgres` and a password (replace `"password"` with a strong password in the examples).


## Environment Configuration

* **Required Environment Variables:**  (Example)
    * `DATABASE_URL`:  Connection string for your database.
    * `SECRET_KEY`:  A strong, randomly generated secret key for security.
    * `API_KEY_WEATHER`: API key for weather integration.
    * `API_KEY_HAZARD`: API key for hazard monitoring integration.  
    * ... other API keys and configurations

* **Local Development `.env` File Setup:** Create a `.env` file in the root directory (or as appropriate for your project) containing your environment variables:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/ems_db
SECRET_KEY=your_secret_key
API_KEY_WEATHER=your_weather_api_key
API_KEY_HAZARD=your_hazard_api_key
...
```

* **Configuration for Different Environments:** Use a configuration management system (e.g., environment variables, a dedicated configuration file) to manage settings for development, testing, staging, and production environments.


## Running the Application

1. **Start Commands:** (Adjust based on your setup)
   * **Docker:** `docker-compose up -d`
   * **Native:**  Start the backend server (e.g., `uvicorn main:app --reload` if using FastAPI) and the frontend development server (`npm start`).

2. **Access Frontend and Backend:** The frontend will typically be accessible at `http://localhost:3000` and the backend API at `http://localhost:8000` (or the ports specified in your configuration).

3. **API Documentation Access:** Use tools like Swagger UI or Postman to explore and test your REST API endpoints.


## Development Workflow

* **Git Workflow and Branching Strategy:** Use Gitflow or a similar branching strategy (e.g., feature branches for new features, hotfix branches for urgent bug fixes).

* **Code Formatting and Linting Setup:** Configure linters (e.g., `black` and `flake8` for Python, `eslint` for JavaScript) and integrate them into your IDE and CI/CD pipeline.

* **Testing Procedures:**  Write unit tests and integration tests. Use a testing framework (e.g., `pytest` for Python, `Jest` for JavaScript).

* **Debugging Setup:** Use your IDE's debugger or command-line debuggers (e.g., `pdb` for Python, browser developer tools for JavaScript).


## Database Management

* **Running Migrations:** Use a database migration tool (e.g., Alembic for SQLAlchemy) to manage database schema changes.

* **Seeding Development Data:** Create scripts to populate your database with sample data for development and testing.

* **Database Reset Procedures:**  Implement scripts to easily reset the database to a clean state.


## Testing

* **Running Unit Tests:**  Execute unit tests using your chosen testing framework (e.g., `pytest` - `pytest` or `Jest` - `npm test`).

* **Running Integration Tests:** Run integration tests to verify interactions between different components of the system.

* **Test Coverage Reports:** Generate test coverage reports to track the percentage of code covered by tests.


## Common Development Tasks

* **Adding New API Endpoints:**  Follow the project's API design guidelines and add new endpoints in the backend, update the API documentation, and add corresponding frontend components.

* **Adding New Frontend Components:** Develop new components using React, Vue, Angular (or your chosen framework), ensure they integrate seamlessly with the backend API, and update the frontend routing.

* **Database Schema Changes:** Use migrations to manage schema changes, update models, and ensure data consistency.

* **Adding Dependencies:** Add dependencies to `requirements.txt` (backend) and `package.json` (frontend) and run `pip install -r requirements.txt` and `npm install` respectively.


## Troubleshooting

* **Common Setup Issues:** Refer to the specific error messages and consult online resources or the project's documentation.

* **Port Conflicts Resolution:** Change port numbers in your configuration files if you encounter port conflicts.

* **Dependency Issues:** Carefully review your `requirements.txt` and `package.json` files for dependency conflicts. Use tools like `pip-tools` to manage dependencies.

* **Environment Variable Problems:** Double-check that your environment variables are correctly set and accessible to your application.


## Contributing

* **Code Style Guidelines:** Adhere to the project's code style guidelines (e.g., PEP 8 for Python,  Airbnb JavaScript Style Guide).

* **Pull Request Process:** Create pull requests for code changes, provide clear descriptions, and address code review feedback.

* **Issue Reporting:** Report issues using the project's issue tracker, providing detailed descriptions and reproduction steps.


Remember to replace placeholder values (like `<repository_url>`, `your_secret_key`, etc.) with your actual values.  This guide provides a general framework; adapt it to the specific technologies and structure of your project.
