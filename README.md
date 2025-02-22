# Custom-LLM-with-Llama2

This repository contains my code for an article writer powered by a custom LLM built on top of the Llama2 base model. I built this project to experiment with and showcase how to generate articles using a Streamlit web interface. The application allows users to input a topic, specify a word count, and select a target audience (e.g., Common Users, Data Scientists, or PhD Students) to generate tailored articles.

![Demo Image](https://github.com/rohan-patnaik/Custom-LLM-with-Llama2/assets/22250758/d9956870-4a6b-40fa-a106-d5e87f0ec2dc)

## Overview

Custom-LLM-with-Llama2 leverages the CTransformers library along with LangChain to communicate with a Llama2 model. I use a prompt template to craft article requests, making it easy to generate content for various job profiles and topics. This project is a work in progress and will soon evolve into a full end-to-end LLM solution.

## Features

- **Article Generation:** Generate articles on a given topic.
- **Customizable Output:** Specify the desired article length and target audience.
- **Interactive Web Interface:** Built with Streamlit for a user-friendly experience.
- **Powered by Llama2:** Utilizes a Llama2 model via the CTransformers library.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/rohan-patnaik/Custom-LLM-with-Llama2.git
   cd Custom-LLM-with-Llama2
   ```

2. **Install Dependencies:**

   Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**

   Start the Streamlit app by executing:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the App:**

   - Enter a topic for the article.
   - Specify the desired number of words.
   - Select the target audience.
   - Click the **Generate** button to see the article generated directly in your browser.

## Future Improvements

I plan to enhance this project into a full end-to-end LLM solution, including further fine-tuning of the model, additional customization options, and improved UI/UX.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---




