# Log Anomaly Detection using RAG(Retrieval Augmented Generation)

## Overview

This project is designed for detecting anomalies in log data using RAG (Retrieval Augmented Generation). This tool combines RAG to efficiently retrieve relevant information from logs and generation models to identify anomalies, providing a robust solution for log anomaly detection.

![image](https://github.com/gypark94/RAGprompt/assets/25690002/55f891f9-bfc3-4283-8492-efa96028e234)


## Features

- **RAG Integration**: Utilize the power of RAG to improve anomaly detection accuracy.
- **Log Retrieval**: Efficiently retrieve relevant log data using retriever models.
- **Anomaly Detection**: Leverage generation models to identify and flag anomalies in log entries.
- **Configurable Thresholds**: Fine-tune detection thresholds to adapt to specific use cases.

## Installation

bash
pip install ragpromt


## Model
Mistral-7B-Instruct-v0.2-GGUF(https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)

## Development Environment
Google Colab

## Configuration
You can customize the behavior of ADRAG by adjusting configuration parameters. Refer to CONFIGURATION.md for detailed instructions.

## Contributing
If you'd like to contribute to ADRAG, please check out our contribution guidelines.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the Hugging Face community for their contributions to the underlying transformer models.
Contact
For any questions or feedback, please contact us at gypark@korea.ac.kr

## References
https://python.langchain.com/docs/use_cases/question_answering/

https://huggingface.co/models?sort=trending&search=gguf.

Liu, Yilun, et al. "Logprompt: Prompt engineering towards zero-shot and interpretable log analysis." arXiv preprint arXiv:2308.07610 (2023).
