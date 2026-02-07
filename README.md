# AI Summarizer

A simple yet powerful text summarization application built with **Streamlit** and **Google's Gemini 2.5 Flash API**. This tool quickly generates concise summaries of any text input using advanced AI technology.

---

## 🚀 Features

- **Fast Summarization**: Powered by Gemini 2.5 Flash, one of the fastest AI models
- **User-Friendly Interface**: Clean and intuitive Streamlit-based web interface
- **Bullet-Point Summaries**: Results are presented as 3 concise bullet points
- **Error Handling**: Comprehensive error handling for API issues and rate limits
- **Secure API Management**: Environment-based API key management using `.env` files

---

## 📋 Requirements

- Python 3.8+
- `streamlit`
- `google-genai`
- `python-dotenv`

---

## 🔧 Installation

### 1. Clone or download the project
```bash
cd ai_summarizer
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**On Windows (PowerShell):**
```powershell
& .\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install streamlit google-genai python-dotenv
```

---

## 🔑 Setup API Key

### 1. Get your Google API Key
1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy your API key

### 2. Create a `.env` file
Create a file named `.env` in the project root directory:

```bash
touch .env
```

### 3. Add your API key
```env
GOOGLE_API_KEY=your_api_key_here
```

**⚠️ Important**: Never commit the `.env` file to version control. Add it to `.gitignore`:

```
.env
```

---

## 🎯 Usage

### Run the application
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### How to use:
1. Paste your text in the text area
2. Click the **"Summarize"** button
3. Wait for the AI to process
4. View your 3-bullet-point summary

---

## 📝 How It Works

```
User Input
    ↓
Streamlit UI captures text
    ↓
Send to Gemini 2.5 Flash API
    ↓
Model generates 3-bullet summary
    ↓
Display results to user
```

The application sends your text to Google's Gemini 2.5 Flash model with a prompt to generate a concise 3-bullet-point summary.

---

## ⚠️ Error Handling

The app handles common API errors gracefully:

| Error | Cause | Solution |
|-------|-------|----------|
| **404 Error** | Model name is incorrect or retired | Check [Google AI Studio](https://aistudio.google.com) for latest model IDs |
| **429 Error** | API quota exceeded | Wait 1 minute before retrying |
| **Other API Errors** | Various API issues | Check API key validity and internet connection |
| **Empty Input** | No text provided | Paste text before clicking Summarize |

---

## 🏗️ Project Structure

```
ai_summarizer/
├── app.py              # Main application file
├── .env                # Environment variables (not tracked in git)
├── .env.example        # Example environment file
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── .venv/              # Virtual environment (optional)
```

---

## 🔒 Security

- **API Keys**: Never hardcode API keys. Always use environment variables
- **Environment Files**: Keep `.env` files out of version control
- **Best Practice**: Use `.env.example` to show required variables without exposing secrets

---

## 📚 Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Generative AI](https://ai.google.dev/)** - Gemini 2.5 Flash API
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management

---

## 🤝 Contributing

Feel free to fork, modify, and improve this project. Suggested improvements:
- Add support for multiple languages
- Implement adjustable summary lengths
- Add file upload functionality
- Support for different summary formats (paragraphs, numbered list, etc.)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🆘 Troubleshooting

### App won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're in the correct virtual environment

### API Key not recognized
- Verify the `.env` file exists in the project root
- Confirm `GOOGLE_API_KEY=` matches exactly in `.env`
- Restart the Streamlit app after updating `.env`

### Slow response times
- Gemini 2.5 Flash is optimized for speed; slower responses may indicate API issues
- Check your internet connection

---

## 📧 Support

For issues or questions, refer to:
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI Documentation](https://ai.google.dev/gemini-2-5/)

---

**Made with ⚡ and AI**
