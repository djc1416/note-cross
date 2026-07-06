# Note&Cross
Stanford University (Code in Place) - Final Project
Author: David Jimenez

Note&Cross is a command-line interface (CLI) task manager written in Python. The application provides local data persistence to manage, track, and log daily operations and pending objectives through a flat-file storage system.

---

## Technical Features

* Data Persistence: Uses the Python os module to handle file system verification and stream updates directly to a local text archive using UTF-8 encoding.
* Input Validation: Implements runtime exception handling via try-except blocks to catch ValueError anomalies during user type conversion.
* Modular Architecture: Separates system logic into distinct operational layers for data loading, state synchronization, and main process execution loop.
* Dynamic Indexing: Utilizes tracking loops to dynamically re-index active elements whenever items are removed or updated.

---

## Technical Specifications

* Language: Python 3.x
* Standard Libraries: os
* Storage Architecture: Flat-file system (my_tasks.txt)

---

## Core Operations

1. Task Registration: Appends strings to the memory array with optional conditional formatting for deadlines.
2. Index-Based Removal: Disposes of targeted array elements based on user-selected numeric indexes.
3. Batch Reset: Flushes the memory array and mirrors the state to the storage archive after user confirmation.
4. Auto-Commit on Exit: Synchronizes the current array state to disk prior to process termination.

---

## Deployment and Execution

Prerequisites: Python 3 installed on the host system.

1. Clone the repository:
   git clone https://github.com/djc1416/note-cross

2. Navigate to the project directory:
   cd note-cross

3. Execute the script:
   python main.py

The application automatically initializes the reference storage file during the first execution cycle if no prior database file is found.
