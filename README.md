# dbt Orchestration Template

A production-ready template for orchestrating data transformations on Snowflake using Apache Airflow with Astronomer. This template provides a scalable and maintainable foundation for building automated data pipelines in a modern cloud data stack.

## 🚀 Features

- **Snowflake Support**: Optimized for Snowflake data warehouse
- **Airflow Orchestration**: Powered by Apache Airflow with Astronomer
- **Containerized Environment**: Docker-based development and deployment
- **Development Tools**: Includes Jupyter notebooks for development and testing
- **Modular Structure**: Organized project structure for easy maintenance

## 📁 Project Structure

```
.
├── data/                          # Data files and sample datasets
├── notebooks/                     # Jupyter notebooks for development
├── orchestration/                 # Airflow orchestration setup
│   ├── dags/                      # Airflow DAG definitions
│   │   ├── dbt/                   # dbt project files and models
│   │   ├── transformation_dag.py  # Main DAG for dbt transformations
│   │   └── .airflowignore
│   ├── plugins/                   # Custom Airflow plugins
│   ├── include/                   # Shared resources
│   ├── tests/                     # Airflow DAG tests
│   ├── .astro/                    # Astronomer configuration
│   ├── Dockerfile                 # Container configuration
│   ├── requirements.txt           # Python dependencies
│   ├── packages.txt               # System packages
│   ├── airflow_settings.yaml      # Airflow configuration
│   ├── .env                       # Environment variables
│   └── .dockerignore              # Docker ignore rules
└── requirements.txt               # Main project dependencies

```

## 🛠️ Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Snowflake account
- Astronomer CLI

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dbt_orchestration_template
   ```

2. **Set up Python environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   - Copy `.env.example` to `.env`
   - Update the variables with your Snowflake credentials and other configurations

4. **Set up Airflow with Astronomer**
   ```bash
   cd orchestration
   
   # Starting the project
   astro dev start --wait 5m
   
   # When finished working
   astro dev stop
   ```

5. **Set up dbt project**
   ```bash
   cd orchestration/dags/dbt
   dbt init # then set up dbt with <your_dbt_project_name>
   ```

6. **Configure Transformation DAG**
   - Navigate to `orchestration/dags/transformation_dag.py`
   - Update the following parameters:
     ```python
     # Update these values in the DbtDag configuration
     your_project_name = "<your_dbt_project_name>"  # Your dbt project name
     dbt_profile_name = "<your_dbt_profile_name>" # Your dbt profile name
     dag_id = "<your_dag_id>"     # Your preferred DAG ID
     ```

7. **Set up Snowflake Connection in Airflow**
   - Open Airflow UI at `http://localhost:8080`
   - Go to Admin → Connections
   - Click "Add a new record" → name it `snowflake_conn`
   - Fill in the connection details:
     - Connection Id: `snowflake_conn`
     - Connection Type: `Snowflake`
     - Host: `your-account.snowflakecomputing.com`
     - Schema: `your_schema`
     - Login: `your_username`
     - Password: `your_password`
     - Account: `your_account`
     - Database: `your_database`
     - Warehouse: `your_warehouse`
     - Role: `your_role`

## 🚀 Usage

1. **Start the development environment**
   ```bash
   cd orchestration
   
   # Starting the project
   astro dev start --wait 5m
   
   # When finished working
   astro dev stop
   ```

2. **Access Airflow UI**
   - Open `http://localhost:8080` in your browser
   - Default credentials: admin/admin

3. **Work with dbt**
   ```bash
   cd orchestration/dags/<your_dbt_project_name>
   dbt run
   ```

## 🔧 Development

- Use Jupyter notebooks in the `notebooks/` directory for development and testing
- Add new DAGs in the `orchestration/dags/` directory
- Develop dbt models within the `orchestration/dags/dbt/<your_dbt_project_name>` directory

## 📚 Documentation

- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Astronomer Documentation](https://docs.astronomer.io/)
- [Snowflake Documentation](https://docs.snowflake.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 