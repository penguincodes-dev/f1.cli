# F1 CLI

A simple command-line interface for quickly viewing Formula 1 championship standings, race schedules, race results, and driver/team information directly from your terminal.

## Features

* View current driver and constructor championship standings
* Display standings with points charts
* Check the next race and session schedule
* View the latest race results
* Look up driver and team information
* View Wikipedia descriptions for drivers and teams
* Browse available driver and team IDs

## Installation

### Requirements

* Python 3.10 or newer
* pipx
* Internet connection

### Install with pipx

`pipx` installs the CLI in an isolated Python environment while making the command available globally.

#### Arch Linux

```bash
sudo pacman -S python-pipx
pipx ensurepath
```

Restart your terminal after running `pipx ensurepath`.

#### Clone the repository

```bash
git clone https://github.com/penguincodes-dev/f1.cli.git
cd f1.cli
```

#### Install the CLI

```bash
pipx install .
```

After installation, the `f1cli` command will be available globally.

## Usage

Start the CLI with:

```bash
f1cli
```

### Championship

| Command      | Description                                     |
| ------------ | ----------------------------------------------- |
| `dStandings` | Show current driver championship standings      |
| `tStandings` | Show current constructor championship standings |
| `dChart`     | Show driver standings with a points chart       |
| `tChart`     | Show constructor standings with a points chart  |

### Races

| Command    | Description                              |
| ---------- | ---------------------------------------- |
| `nextRace` | Show the next race and session schedule  |
| `lastRace` | Show the results of the most recent race |

### Driver & Team Information

| Command          | Description                                       |
| ---------------- | ------------------------------------------------- |
| `driverIds`      | List all available driver IDs                     |
| `teamIds`        | List all available team IDs                       |
| `dInfo <driver>` | Show driver information and Wikipedia description |
| `tInfo <team>`   | Show team information and Wikipedia description   |

For `dInfo` and `tInfo`, use `driverIds` or `teamIds` first to find the required ID.

### General

| Command  | Description        |
| -------- | ------------------ |
| `help`   | Show the help menu |
| `clear`  | Clear the terminal |
| `exit`   | Exit the F1 CLI    |
| `Ctrl+C` | Exit the F1 CLI    |

## Updating

Pull the latest changes and reinstall the package:

```bash
git pull
pipx install . --force
```

## Uninstall

```bash
pipx uninstall f1-cli
```

## License

See the repository for license information.
