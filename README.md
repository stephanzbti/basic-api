# Base Python Application

## API

The API is desing to have a easy understanding. The folder is divide with this rules:

```
- src/config -> Created to have only one folder with all configurations files
- src/config/config.py -> Have all configurations about environment variables.
- src/routes -> Created to have all informations about routes, so, to have a better organization arround filed, we can create subfolder with routes.
- src/routes/routes.py -> Principal routes file.
- main.py -> Application start.
```

We are using `Flask` to create our `API`. The project is easier as it is understand.

To work with this project you will need:

| Binary | Version | Checked Version    |
| ------ | ------- | ------------------ |
| python | 3.8.9   | :white_check_mark: |

### Install dependencies

To install python dependencies you can run:

```
pip install -r requirements.txt
```

### Execution

To run this project you need to install the `dependencies` and then execute the command above:

```
python main.py
```

### Environments

| Environment  | Description           | Type   | Default       |
| ------------ | --------------------- | ------ | ------------- |
| LOG_LEVEL    | Service Log Level     | String | "INFO"        |
| HOST_BINDING | Host binding IP       | String | "0.0.0.0"     |
| HOST_PORT    | Host listen Port      | String | "8080"        |
| ENVIRONMENT  | Execution Environment | String | "development" |

## Kubernetes Files

To work with this project you will need:

| Binary             | Version | Checked Version    |
| ------------------ | ------- | ------------------ |
| Kubernetes Cluster | v1.21   | :white_check_mark: |

TO DO: Create a Helm Chart to deploy it because it's better to use `Helm` on automating creating releases.
