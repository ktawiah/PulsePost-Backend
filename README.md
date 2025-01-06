# PulsePost App Backend

<!-- ##### <b>`Under Construction 🔨`</b> -->

This project is the backend for PulsePost, a blog app designed to provide a seamless and intuitive platform for users to publish and share their thoughts, articles, and experiences with a wide audience. It aims to offer features such as customizable user profiles, a robust content management system, social sharing capabilities, and analytics to help bloggers track their impact and engagement.
Click here 👉 for Frontend App ~ [PulsePost Frontend](https://github.com/ktawiah/PulsePost-Frontend/)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- Email and Password Authentication
- Github and Google OAuth2 support
- HttpOnly cookie authentication

## Prerequisites

- Python 3.x
- [Poetry](https://python-poetry.org/)
- (Optional) SendGrid account for email functionality

## Image of Web API

<img src="https://github.com/ktawiah/PulsePost-Backend/blob/main/images/PulsePost2.png" alt="Screenshot"/>

## Getting Started

Follow these instructions to set up this project locally on your device.

#### 1. Clone the repository and navigate to project directory

```bash
git clone https://github.com/ktawiah/PulsePost-Backend.git
```

#### 2. Install Poetry (if not already installed)

Navigate to poetry to install the latest version. Click [here](https://python-poetry.org/docs/) to proceed

#### 3. Install project dependencies

```bash
  make install
```

#### 4. Setup environment variables

Create a .env file in the project root and add the following variables:

```
DEVELOPMENT_MODE=True

AUTH_COOKIE_SECURE=False

DJANGO_SETTINGS_MODULE="settings"

DJANGO_CONFIGURATION=Local

DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

# Add you google client ID
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=""

# Add you google client secret
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=""

# Add you github client ID
SOCIAL_AUTH_GITHUB_KEY=""

# Add you google client secret
SOCIAL_AUTH_GITHUB_SECRET=""

# Add redirect URIS as specified in your OAuth Apps. Egs. "http://localhost:3000/api/auth/google,http://localhost:3000/api/auth/github"
SOCIAL_AUTH_ALLOWED_REDIRECT_URIS=""

# (Optional) Add your email settings. This project used send grid.
SENDGRID_API_KEY=""

# Add your default from email
DEFAULT_FROM_EMAIL=""
```

#### 5. Run migrations

```bash
  make makemigrations

  make migrate
```

#### 6. Start the backend development server

```bash
  make runserver
```

#### Note: Explore other development commands in the Makefile.

## Usage

Once the backend server is running, you can interact with the API. Below are a few example endpoints:

- #### User Registration: POST /api/auth/register/

- #### User Login: POST /api/auth/login/

<!-- - #### Create Post: POST /api/posts/

- #### Get Posts: GET /api/posts/ -->

Refer to the API documentation for more details.

## Contributing
Contributions to this project are welcomed! If you have any issues with the project or have some ideas for enhancements to contribute, please don't hesitate to open an issue or submit a pull request. Your input is much appreciated.
