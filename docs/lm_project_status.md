# Project Status

This document provides a structured overview of the project for the language model (LM). It lists all the files in the project, their purpose, dependencies, and current status. This document is intended to facilitate the transition to a different language model if necessary.

Written by Codebuddy, an AI assistant.

## Files

- `app.py`: The main entry point of the application. It is responsible for coordinating the various functionalities provided by other modules.
- `tts.py`: This file contains the text-to-speech (TTS) functionality.
- `sr.py`: This file contains the speech recognition (SR) functionality.
- `message_handler.py`: This file is responsible for reading and responding to messages.
- `minstral.py`: This file handles the integration with Minstral 7B LLM.
- `interactive_features.py`: This file contains various interactive features such as TTS & SR Language Learning, Language Pronunciation Trainer, Interactive Storytelling, and Storytime for Kids.
- `voice_control.py`: This file contains voice control features such as Voice Memo Reminder, Speech-Based To-Do List, Voice-Controlled Alarm Clock, and Voice-Activated Calculator.
- `tts_tools.py`: This file contains the Offline TTS Audiobook Maker functionality.

## Dependencies

The project has the following dependencies:

- `pyttsx3`: A Python library for text-to-speech conversion.
- `speech_recognition`: A Python library for performing speech recognition.

For a comprehensive list of potential dependencies, please refer to the [Preliminary Dependencies](./preliminary_dependencies.md) document.

## Current Status

The project is currently under development. The `app.py` file has been created and serves as the main entry point of the application. The `tts.py` and `sr.py` files have been created and contain the basic TTS and SR functionalities, respectively. The `message_handler.py`, `minstral.py`, `interactive_features.py`, `voice_control.py`, and `tts_tools.py` files have been created but do not yet contain any functionality.