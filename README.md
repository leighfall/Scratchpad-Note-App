# Scratchpad Note App

This project creates a note-taking app that currently completes some basic functions:

    - Insert a Note: Main window allows you to start typing notes.
    - Save: Allows you to save the note to your computer.
    - Open: Allows you to retrieve a saved note from your computer.
    - Format Text: Provides a variety of options to specialize your notes

## Requirements and Dependencies

Requires current versions of Python and PyQT5.

## Installation

Clone the repository for access to all necessary files.

## Running the Application

From the Command-Line:

```bash
"Path to python executable"/python.exe "Path to cloned repo"/main.py
```

## Files Included

main.py -> Runs the main application.

note_widget.py -> Controls the box where notes are actually typed. This file is imported into note_window.py.

note_window.py -> Main application window that holds the toolbar and box for notes. This file is imported into main.py.

search.py -> Creates a search function.

(Scrapped Feature) calendar.py -> Creates a function for adding notifications for note-retrieval on certain days. 

nwid.qss, nwin.qss, sb.qss -> Cascading style sheet for the application.

landpage_window.py -> Creates a start point for the app.

landpage_widget.py -> Controls actual landing page widget.

## Roadmap

Complete Landing Page for the Applications

Potential Website for Download

## Contributors

<a href="https://github.com/leighfall/" target="_blank">leighfall</a> - Completed qss portion
<br><a href="https://github.com/swhite83" target="_blank">swhite83</a> - Completed python portion
<br><a href="https://github.com/asuther8" target="_blank">asuther8</a> - Completed Search Bar
