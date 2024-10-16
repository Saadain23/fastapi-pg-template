<h1>🚀 FastAPI PostgreSQL Backend Template</h1>

<p>Welcome to the <b>FastAPI PostgreSQL Backend Template</b>, a ready-to-use foundation for building scalable, high-performance backends with <b>FastAPI</b> and <b>PostgreSQL</b>. This template includes essential configurations, user authentication, security with JWT tokens, and a well-structured repository layout — all set up to kickstart your development quickly and efficiently!</p>

<h2>🎯 Features</h2>

<ul>
  <li><b>FastAPI Framework</b>: Benefit from FastAPI’s lightning-fast performance and intuitive development experience with asynchronous support.</li>
  <li><b>PostgreSQL Integration</b>: Pre-configured PostgreSQL database connection using SQLAlchemy.</li>
  <li><b>JWT Authentication</b>: Secure user authentication and authorization using JSON Web Tokens (JWT).</li>
  <li><b>Modular and Clean Structure</b>: Follow a well-organized project layout with clear separation of concerns (e.g., models, routers, services).</li>
  <li><b>Alembic for Migrations</b>: Seamlessly manage database migrations with Alembic, ensuring your schema stays in sync across environments.</li>
  <li><b>Dependency Injection</b>: Leverage FastAPI’s powerful dependency injection system for flexible and testable code.</li>
  <li><b>Environment Variables Configuration</b>: Use <code>.env</code> files to manage database credentials, secret keys, and other environment-specific settings.</li>
</ul>

<h2>🗂️ Project Structure</h2>

<pre>
fastapi-pg-template/
├── alembic/                # Alembic configuration and migration scripts
├── app/
│   ├── api/                # API endpoints (routers)
│   ├── core/               # Core configurations (settings, security, JWT)
│   ├── db/                 # Database connection and models
│   ├── services/           # Business logic and services
│   ├── models/             # Database models (SQLAlchemy)
│   ├── schemas/            # Pydantic models (validation and serialization)
│   └── main.py             # Application entry point
├── .env                    # Environment variables for sensitive data (not committed)
├── alembic.ini             # Alembic configuration file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
</pre>

<h2>🔧 Quick Start</h2>

<h3>1. Clone the repository</h3>
<pre>
git clone https://github.com/your-username/fastapi-pg-template.git
cd fastapi-pg-template
</pre>

<h3>2. Set up a virtual environment</h3>
<pre>
<h4>Create a virtual environment</h4>
python3 -m venv venv

<h3>Activate the virtual environment</h3>
<h4>On Linux/macOS:</h4>
source venv/bin/activate
<h4>On Windows:</h4>
venv\Scripts\activate
</pre>

<h3>3. Install the dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>4. Configure environment variables</h3>
<p>Create a <code>.env</code> file in the root directory with your database connection information and JWT secret:</p>

<pre>
DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=token_expiry(in minutes)
ALGORITHM=
</pre>

<h3>5. Initialize the database</h3>
<p>Run Alembic migrations to set up your PostgreSQL database schema:</p>

<pre>
alembic upgrade head
</pre>

<h3>6. Run the FastAPI server</h3>
<p>Start the FastAPI development server:</p>

<pre>
uvicorn app.main:app --reload
</pre>

<p>Your API is now running on <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>.</p>

<h2>📜 API Documentation</h2>

<p>FastAPI automatically generates interactive API documentation:</p>

<ul>
  <li>Swagger UI: <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a></li>
  <li>ReDoc: <a href="http://127.0.0.1:8000/redoc">http://127.0.0.1:8000/redoc</a></li>
</ul>

<h2>🛠️ Development and Migration Workflow</h2>

<ol>
  <li><b>Create a New Migration</b>: After modifying models, generate a new Alembic migration:
    <pre>alembic revision --autogenerate -m "Describe changes here"</pre>
  </li>

  <li><b>Apply Migrations</b>: Apply all pending migrations:
    <pre>alembic upgrade head</pre>
  </li>

  <li><b>Rollback Migrations</b> (IF NEEDED):
    <pre>alembic downgrade -1</pre>
  </li>
</ol>

<h2>🔐 Authentication</h2>
<p>The template includes JWT-based authentication for secure user login and access control. You can customize the authentication logic in <code>app/core/security.py</code> and define routes in <code>app/api/endpoints/auth.py</code>.</p>

<h2>🛠️ Customization</h2>
<p>This template is designed to be flexible and easily customizable. Here are a few ideas:</p>

<ul>
  <li><b>Add new models and migrations</b> for additional database tables.</li>
  <li><b>Extend authentication logic</b> with OAuth2, social logins, or role-based access control (RBAC).</li>
  <li><b>Add new API endpoints</b> by creating more routers under <code>app/api/endpoints</code>.</li>
</ul>

<h2>🧪 Testing</h2>
<p>To ensure that everything works as expected, you can add unit tests with <code>pytest</code> or similar testing frameworks. FastAPI also makes it easy to test your routes and services.</p>

<pre># Example of running tests
pytest
</pre>

<h2>💡 Contributing</h2>
<p>Contributions are welcome! If you'd like to enhance this template, feel free to submit pull requests or open issues.</p>

<h2>📄 License</h2>
<p>This repository is licensed under the GPL License. See the <a href="./LICENSE">LICENSE</a> file for details.</p>

<hr/>

<h3>🎉 Start building your next FastAPI project faster with this fully equipped template! Happy coding! 💻</h3>
