# Digital Twin Application

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

AI-powered digital twin chat application that creates intelligent company representatives using AWS Bedrock Knowledge Base and Strands agents.

## 🚀 Features

- **Multi-Company Support**: Chat with different company representatives
- **Session Management**: Persistent chat sessions with history
- **Knowledge Base Integration**: AWS Bedrock Knowledge Base for accurate responses
- **Professional UI**: Clean, modern interface inspired by ChatGPT
- **Intelligent Responses**: AI-powered responses using Strands agents

## 📋 Requirements

- Python 3.8+
- AWS Bedrock access
- Flotorch API access

## 🛠️ Installation

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd digital-twin
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   ```bash
   export SHARED_KNOWLEDGE_BASE_ID="your-knowledge-base-id"
   export KNOWLEDGE_BASE_SOURCE_ID="your-source-id"
   export FLOTORCH_API_KEY="your-flotorch-api-key"
   export FLOTORCH_BASE_URL="your-flotorch-base-url"
   export FLOTORCH_MODEL_ID="your-model-id"
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

### Development Setup

```bash
# Install development dependencies
make install-dev

# Setup pre-commit hooks
make setup

# Run tests
make test
```

## 🐳 Docker Deployment

```bash
# Using Docker Compose
docker-compose up -d

# Or using Docker directly
make docker-build
make docker-run
```

## 📖 Usage

1. **Select Company**: Choose from TechCorp, FinanceInc, HealthPlus, or RetailMax
2. **Start Chat**: Click "New Chat" or select a previous conversation
3. **Ask Questions**: Type questions about the selected company
4. **Switch Companies**: Change companies while maintaining session context
5. **Manage Sessions**: View, switch, or delete chat sessions

## 🏗️ Project Structure

```
digital-twin/
├── src/
│   └── digital_twin/          # Main application package
│       ├── app.py            # Streamlit application
│       ├── service.py        # Main service layer
│       ├── agent.py          # Strands agent management
│       ├── knowledge_base.py # Knowledge base client
│       └── config.py         # Configuration management
├── tests/                    # Test suite
├── docs/                     # Documentation
├── main.py                   # Application entry point
├── requirements.txt          # Dependencies
├── pyproject.toml           # Project configuration
├── Makefile                 # Development commands
├── Dockerfile               # Docker configuration
└── docker-compose.yml       # Docker Compose configuration
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SHARED_KNOWLEDGE_BASE_ID` | AWS Bedrock Knowledge Base ID | Yes |
| `KNOWLEDGE_BASE_SOURCE_ID` | Knowledge Base Source ID | Yes |
| `FLOTORCH_API_KEY` | Flotorch API key | Yes |
| `FLOTORCH_BASE_URL` | Flotorch base URL | Yes |
| `FLOTORCH_MODEL_ID` | Flotorch model ID | No |
| `AWS_REGION` | AWS region | No |

### Companies

The application supports four companies:

- **TechCorp**: Technology company specializing in software solutions
- **FinanceInc**: Financial services company providing investment solutions
- **HealthPlus**: Healthcare company focused on medical innovations
- **RetailMax**: Retail company with extensive e-commerce operations

## 🧪 Development

### Available Commands

```bash
make help                 # Show all available commands
make install              # Install the application
make install-dev          # Install development dependencies
make test                 # Run tests
make test-cov             # Run tests with coverage
make lint                 # Run linting
make format               # Format code
make clean                # Clean build artifacts
make run                  # Run the application
```

### Code Quality

The project uses several tools for code quality:

- **Black**: Code formatting
- **Flake8**: Linting
- **MyPy**: Type checking
- **Pytest**: Testing
- **Pre-commit**: Git hooks

## 📚 Documentation

Detailed documentation is available in the [docs/](docs/) directory:

- [Complete Documentation](docs/README.md)
- [API Reference](docs/README.md#api-reference)
- [Configuration Guide](docs/README.md#configuration)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:

- Open an [issue](https://github.com/your-org/digital-twin/issues)
- Check the [documentation](docs/README.md)
- Review the [troubleshooting guide](docs/README.md#troubleshooting)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [AWS Bedrock](https://aws.amazon.com/bedrock/) for knowledge base
- [Flotorch](https://flotorch.ai/) for LLM integration
- [Strands](https://strands.ai/) for agent framework