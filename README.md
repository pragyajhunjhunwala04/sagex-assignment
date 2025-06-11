# CSV Data Transformation Tool using LLM

A simple yet powerful tool that leverages Large Language Models (LLM) to transform CSV data based on natural language commands. Transform any column in your CSV files using intuitive instructions like "translate to French", "summarize in 10 words", or "convert to formal tone".

## Features

- 🔄 **Batch Processing**: Efficiently processes data in configurable batches (10-50 rows per batch)
- 🤖 **LLM Integration**: Uses Google's Gemini AI for intelligent data transformation
- 📊 **CSV Support**: Read, transform, and save CSV files seamlessly
- 🎯 **Smart Prompting**: Automatically clarifies unclear transformation commands
- ⚡ **Progress Tracking**: Real-time progress updates with timing information
- 🔍 **Preview Mode**: Option to preview transformations before processing entire dataset

## Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd sagex-assignment
```

### 2. Install Dependencies
```bash
pip install google-generativeai pandas python-dotenv
```

### 3. Setup API Key
1. Generate your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Tool
```bash
python main.py
```

## Usage

### Interactive Mode
Run the main script and follow the prompts:
1. Select a CSV file from your directory
2. Choose the input column to transform
3. Specify the output column name
4. Enter your transformation command

```

## Transformation Examples

- **Translation**: `"Translate to French"`
- **Summarization**: `"Summarize in 10 words"`
- **Tone Conversion**: `"Convert to a formal tone"`
- **Simplification**: `"Rewrite using simpler language"`
- **Data Enrichment**: `"Find the capital city of this country"`

## File Structure

```
sagex-assignment/
├── main.py           # CLI interface for CSV selection
├── chat.py           # Gemini AI integration
├── processing.py     # Core batch processing logic
├── .env             # API key configuration (create this)
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## Requirements

- Python 3.7+
- Google Generative AI API key
- pandas
- python-dotenv

## Sample Data

The tool works with any CSV file. For the assignment demo, use a CSV with country names to get their most famous cities:

```csv
country
United States
France
Japan
Brazil
```

Output:
```csv
country,famous_city
United States,New York City
France,Paris
Japan,Tokyo
Brazil,Rio de Janeiro
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is part of an internship assignment and is for educational purposes.