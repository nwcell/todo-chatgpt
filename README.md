# Todo App with FastAPI and React

This project is a simple todo app that demonstrates how to build a backend API with FastAPI and a frontend UI with React. The API allows for creating, retrieving, updating, and deleting tasks, and the UI provides a way to interact with these API endpoints.

## Prerequisites

Before you can run this project, you'll need to have the following software installed on your machine:

- [Node.js](https://nodejs.org/) (version 12 or higher)
- [Python 3](https://www.python.org/) (version 3.6 or higher)

## Running the API

To run the API, follow these steps:

1. Navigate to the `api` directory:

```bash
cd api
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the API:

```bash
uvicorn main:app --reload
```

The API should now be running on [http://localhost:8000](http://localhost:8000).

## Running the UI

To run the UI, follow these steps:

1. Navigate to the `ui` directory:

```bash
cd ui
```

2. Install the dependencies:

```bash
npm install
```

3. Run the UI:

```bash
npm start
```

The UI should now be running on [http://localhost:3000](http://localhost:3000).

## Building the UI for production

To build the UI for production, follow these steps:

1. Navigate to the `ui` directory:

```bash
cd ui
```

2. Build the UI:

```bash
npm run build
```

This will create a production-ready build of the UI in the ui/build directory.

## Project structure
This project has the following structure:

* `api`: Contains the code for the FastAPI backend.
* `ui`: Contains the code for the React frontend.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/nwcell/todo-chatgpt/blob/main/LICENSE) file for more details.

I hope this helps! Let me know if you have any questions or need further clarification.
