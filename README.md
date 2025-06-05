# BytesAndCoffee - Project Overview

This repository aggregates several experimental projects. Each subdirectory houses a standalone component with its own documentation. Below is a quick summary of what each folder contains and how to get started.

## QuadShot
A simple CPU, assembler and runtime written in Python.
- **Getting Started**: Run programs with `python QuadShot.py <program_name> <input_string>` as described in [QuadShot/README.md](QuadShot/README.md).
- **Documentation**: Additional notes on the instruction set and runtime are in [QuadShot/docs](QuadShot/docs).

## Telepush
Small utility that pushes messages from a database to Telegram using the Bot API.
- **Getting Started**: Configure the environment variables listed in [Telepush/example.env](Telepush/example.env) and run `python sqlpush.py`. A Dockerfile is also provided.
- **Documentation**: See [Telepush/README.md](Telepush/README.md).

## zlog-sql
ZNC logging plugin that writes IRC logs to MySQL, PostgreSQL or SQLite.
- **Getting Started**: Copy `zlog_sql.py` to your ZNC modules directory, enable `modpython` and load the module with a connection string. The [README](zlog-sql/README.md) lists examples for MySQL, PostgreSQL and SQLite.
- **Documentation**: Screenshot and basic instructions are available in [zlog-sql/docs](zlog-sql/docs).

## zlog-sql-query
Client/server application used to query ZNC logs from a MySQL backend.
- **Getting Started**: Configure the server in `Server/auth.py`, launch `Server/app.py`, then use the PyQt client in `Client/main.py`. Required libraries are noted in [zlog-sql-query/README.md](zlog-sql-query/README.md).

## zlog_parsing
Utilities for parsing IRC logs and managing a processing queue.
- **Getting Started**: Create a `.env` file as shown in [zlog_parsing/readme.md](zlog_parsing/readme.md), then run `python parse_logs.py` and `python zlog_queue.py`. Docker instructions are also provided.
- **Documentation**: See the detailed guides in [zlog_parsing/docs](zlog_parsing/docs).


## Testing

A small pytest suite covers the standalone modules. After installing `pytest`, run

```sh
pytest
```

from the repository root.
