# Twitter ETL with Airflow

This project demonstrates how to use Apache Airflow to perform an ETL process for fetching tweets from Twitter, processing them, and storing the results in a CSV file.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [DAG Configuration](#dag-configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases the utilization of Apache Airflow, Tweepy, and Pandas to create an ETL pipeline that extracts tweets from a specified Twitter account, transforms the data, and loads it into a CSV file. The pipeline is orchestrated using Apache Airflow's Directed Acyclic Graphs (DAGs).

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/twitter-etl-airflow.git
   cd twitter-etl-airflow
   ```

2. Install the required Python libraries using pip:

   ```bash
   pip install tweepy pandas apache-airflow
   ```

3. Configure your Twitter API credentials in `twitter_etl.py`. Replace the placeholders with your actual API keys and tokens.

4. Configure your Apache Airflow settings in `twitter_dag.py`. You can customize the DAG's name, default arguments, schedule interval, and more.

## Usage

1. Start the Airflow web server:

   ```bash
   airflow webserver -p 8080
   ```

2. Start the Airflow scheduler in a separate terminal:

   ```bash
   airflow scheduler
   ```

3. Access the Airflow UI by opening a web browser and navigating to `http://localhost:8080`.

4. Enable and trigger the "twitter_dag" DAG from the UI.

## DAG Configuration

The DAG is configured in the `twitter_dag.py` script. Here are some key configuration options:

- `default_args`: This dictionary contains default settings for the DAG, such as the owner, start date, email notifications, retries, and retry delay.

- `dag`: The DAG object is created with a name, default arguments, description, and schedule interval. Adjust these values to suit your requirements.

- `PythonOperator`: The task that executes the ETL process is defined using the `PythonOperator`. Modify the `python_callable` parameter to point to your ETL function.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
