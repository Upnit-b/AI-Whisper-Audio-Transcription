# 🎙️ Audio Translation App

A modern Flask-based web application that transcribes and translates audio files using OpenAI's Whisper and GPT models. Upload an audio file in any language, and get an instant translation to your target language.

## ✨ Features

- 🎵 **Audio Upload**: Support for MP3 and other common audio formats
- 🔊 **Speech-to-Text**: Automatic transcription using OpenAI Whisper API
- 🌍 **Multi-language Translation**: Translate transcribed text to any language using GPT
- 🎨 **Modern UI**: Clean, responsive interface built with HTML/CSS
- ⚡ **Fast Processing**: Quick audio processing and translation
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **AI/ML**: OpenAI API (Whisper for transcription, GPT for translation)
- **Frontend**: HTML5, CSS3
- **Environment Management**: python-dotenv

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Upnit-b/OpenAI-Whisper-Audio-Transcription-Translation
   cd Project-2
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root directory:

   ```bash
   touch .env
   ```

   Add your OpenAI API key to the `.env` file:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## ⚙️ Configuration

The application uses the following configuration:

- **Upload Folder**: `static/` - Where uploaded audio files are stored
- **Server Host**: `0.0.0.0` - Accessible from any network interface
- **Server Port**: `8080`
- **Debug Mode**: Enabled (disable in production)

## 💻 Usage

### Running the Application

1. **Start the Flask server**

   ```bash
   python app.py
   ```

2. **Access the application**

   Open your web browser and navigate to:

   ```
   http://localhost:8080
   ```

3. **Upload and Translate**
   - Click "Choose File" and select an audio file (MP3 format recommended)
   - Enter the target language (e.g., "French", "Spanish", "Japanese")
   - Click "Upload" to process the file
   - The translated text will be returned as JSON

### Running the Demo Script

To test the transcription functionality independently:

```bash
python demo.py
```

This will transcribe the `recording.mp3` file and print the English transcription.

## 📁 Project Structure

```
Project-2/
│
├── app.py                 # Main Flask application
├── demo.py               # Standalone transcription demo
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
│
├── static/              # Static files and uploaded audio
│   └── recording.mp3    # Sample/uploaded audio files
│
├── templates/           # HTML templates
│   └── index.html      # Main upload interface
│
└── venv/               # Virtual environment (auto-generated)
```

## 🔌 API Endpoints

### `GET /`

Returns the main upload interface.

### `POST /`

Processes audio file upload and returns translation.

**Request:**

- Method: POST
- Content-Type: multipart/form-data
- Parameters:
  - `file`: Audio file (required)
  - `language`: Target language for translation (required)

**Response:**

```json
{
  "translation": "Translated text in target language"
}
```

## 🎯 How It Works

1. **Upload**: User uploads an audio file through the web interface
2. **Transcription**: The audio is transcribed to English using OpenAI's Whisper model
3. **Translation**: The English transcription is translated to the target language using GPT
4. **Response**: The translated text is returned to the user

## 📝 Future Enhancements

- [ ] Support for more audio formats (WAV, M4A, OGG)
- [ ] Real-time audio recording from browser
- [ ] Translation history and saved translations
- [ ] Support for multiple file uploads
- [ ] Download translated text as file
- [ ] Audio-to-audio translation with text-to-speech
- [ ] User authentication and API rate limiting

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Upnit Banga\
Software Engineer \| Solutions Engineer \| AI Enthusiast

---

**Note**: This application requires an active OpenAI API account with available credits. API usage will incur costs based on OpenAI's pricing model.
