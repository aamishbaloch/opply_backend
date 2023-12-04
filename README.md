## Opply Backend App

Our backend that is being used for mobile application for our customers, 
so that they can order our products using their phones. 

### Dependencies

- Django v4.2.7
- Docker v20.10.8
- Python v3.9.6

### Usage

Following are the required steps to use this platform.

- Clone the repo
- Update the `.env` file
- Build the image
```sh
$ docker-compose build
```
- Once the image is built, run the container
```sh
$ docker-compose up
```

### Into the machine?

If you want to ssh the container you can use the `makefile`

```sh
$ make ssh
```
then you can use all the django commands.

To generate static files for Django Admin, use:

```sh
$ docker-compose exec app python manage.py collectstatic --no-input --clear
```

### Deployment Guidelines (Bonus)

As we have dockerized our application, we will use AWS ECR which is a 
fully-managed Docker image registry that makes it easy for developers to 
store and manage images. and then we can easily run these containers using AWS ECS.

Links: https://aws.amazon.com/ecr/, https://aws.amazon.com/ecs/