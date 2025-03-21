# 🌿 Herbal Medicine Chatbot

An AI-powered chatbot that extracts and provides medicinal information about herbal plants from a given PDF document. This project uses **Cohere API** for AI-driven responses and **Streamlit** for an interactive user interface.

## 🚀 Features
- Extracts text from a PDF containing herbal medicinal uses.
- Uses Cohere AI to generate responses based on document context.
- Interactive chatbot UI built with Streamlit.

## 🛠 Tech Stack
- **Python**
- **Streamlit** (for UI)
- **Cohere API** (for AI responses)
- **PyPDF2** (for PDF text extraction)
- **dotenv** (for API key management)

## 📜 Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/herbal-medicine-chatbot.git
   cd herbal-medicine-chatbot
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   - Create a `.env` file in the project root and add your **Cohere API Key**:
     ```env
     COHERE_API_KEY=your_cohere_api_key_here
     ```

5. **Run the Application:**
   ```sh
   streamlit run app.py
   ```

## 🏗 Project Structure
```
📂 herbal-medicine-chatbot
├── 📄 app.py              # Main Streamlit app
├── 📄 extract_text.py     # PDF text extraction module
├── 📄 chatbot.py          # Cohere-based chatbot logic
├── 📄 requirements.txt    # Dependencies
├── 📄 README.md           # Project documentation
└── 📄 .env.example        # Sample environment file
```

## 📌 Usage
- Upload a PDF containing herbal medicine information.
- Ask the chatbot about medicinal benefits of herbs.
- The chatbot provides responses based on extracted document data.

## 🤝 Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License
This project is licensed under the **MIT License**.

---

🌱 *Empowering herbal knowledge with AI!* 🚀


