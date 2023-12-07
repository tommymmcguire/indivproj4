[![CI](https://github.com/tommymmcguire/indivproj4/actions/workflows/main.yml/badge.svg)](https://github.com/tommymmcguire/indivproj4/actions/workflows/main.yml)

# Flask Image Generation App with DALL-E and Azure Deployment

## Walk Through [Youtube Video](https://youtu.be/ME6gs6-7vYk)

This project is a Flask web application that utilizes DALL-E to generate images based on user input, which are then overlaid onto a t-shirt template. The application is containerized using Docker and deployed on Azure Web App, with the Docker container hosted on Docker Hub.

To use the pre-deployed App that I created go to [Custom Shirt App](https://customshirt.azurewebsites.net/). Use the text box to input the type of image you would like on your t-shirt. Enjoy and be creative!

*Warning - the API Key that I used may be out of credit or disabled. To run this application on your own follow the instructions below.*

## Example

<img width="411" alt="Screenshot 2023-12-07 at 1 07 14 AM" src="https://github.com/tommymmcguire/indivproj4/assets/141086024/d5c6a48e-857a-45ed-a0cc-ff009a286a85">

<img width="561" alt="Screenshot 2023-12-07 at 1 06 47 AM" src="https://github.com/tommymmcguire/indivproj4/assets/141086024/e6f723e0-3edc-45f5-af6c-b8085fde6413">


## Features

- **Image Generation**: Leveraging DALL-E to generate images based on user-provided descriptions.
- **Image Overlay**: Processing the generated images and overlaying them onto a t-shirt template.
- **Docker Integration**: Containerized Flask application for easy deployment and scalability.
- **Azure Deployment**: Deployed on Azure Web App for high availability and auto-scaling.
- **CI/CD pipeline**: Built with GitHub Actions, automates the development lifecycle processes. The workflow in .github/workflows – main.yml – ensures consistent code quality and streamlined deployment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Azure account (for deployment)
- Docker Hub account (for hosting the container)

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

1. Clone the repository
Makefile and a requirements.txt to install all of the dependencies and assist in formating the code.

      - Install: install dependencies

      - Format: formats the code using black
      
      - All: performs all


`make install` to install, `make format` to format, and `make all` to perform both

You should obtain a OpenAI API key before running the project. The key should be stored `.env` file under the root folder of the project. The `.env` file should look like this:
```
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY=abc123
```

To run using Flask:
Nevigate to the root folder of the project and type the following command in the terminal:
``` 
$ python app.py
```


2. Build the docker container:
`docker build -t your-dockerhub-username/my-flask-app .`
3. Run the container locally:
`docker run -p 5000:80 your-dockerhub-username/my-flask-app`

## Deployment
Instructions for deploying this on a live system using Azure Web App and Docker Hub.

<img width="1427" alt="Azure" src="https://github.com/tommymmcguire/indivproj4/assets/141086024/51bd3ed5-5942-4898-8389-7536c0d0067c">


### Pushing the Container to Docker Hub
1. Tag your docker image:
`docker tag my-flask-app your-dockerhub-username/my-flask-app`
2. Push to Docker Hub:
`docker push your-dockerhub-username/my-flask-app`

### Deploying on Azure Web App
1. Create a Web App in Azure Portal.
2. Configure the Web App to use the Docker container from Docker Hub.
3. Set environment variables if needed.
4. Access the application through the provided Azure URL.
