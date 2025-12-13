# 🤖 Gemini ChatBot

A simple and elegant chatbot built with Streamlit and Google's Gemini AI API.

## Features

- 💬 Interactive chat interface
- 🧠 Powered by Gemini 2.5 Flash
- 💾 Conversation history
- 🎨 Clean and modern UI

## Prerequisites

- Python 3.8 or higher
- Google AI API Key ([Get it here](https://makersuite.google.com/app/apikey))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/gemini-chatbot.git
cd gemini-chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_api_key_here
```

## Usage

Run the application:
```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## Project Structure
```
gemini-chatbot/
│
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in repo)
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```

## Configuration

- **Model**: The app uses `gemini-2.5-flash` by default. You can change it in `main.py`
- **API Key**: Store your Google API key in the `.env` file

## Screenshots

[Add screenshots of your app here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://deepmind.google/technologies/gemini/)

## Support

If you encounter any issues, please [open an issue](https://github.com/YOUR_USERNAME/gemini-chatbot/issues) on GitHub.
