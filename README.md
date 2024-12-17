
# AnimationsInTelegram

This repository contains examples and implementations of various animations that can be used in Telegram bots. The goal is to provide reusable and customizable animation scripts to enhance user experience in Telegram applications.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get a copy of this repository up and running on your local machine, follow the instructions below.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have a Telegram account and a Telegram-application. You can create a new application and get API's from the [official site](https://my.telegram.org/auth).
- You have basic knowledge of how to create and manage Telegram's API.

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/AndreiDarik/AnimationsInTelegram.git
    cd AnimationsInTelegram
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Usage

To use the animations in your Telegram bot, follow these steps:

1. Type in the message line your specific word. You can find/change it in Python file of your animation here: @app.on_message(filters.regex("YOUR_SPECIFIC_WORD"))


## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) to learn how you can contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Do not forget to replace placeholders like `YOUR_API` and `YOUR_SPECIFIC_WORD` with the actual values.
