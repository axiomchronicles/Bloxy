# Bloxy

Bloxy is a user-friendly blogging platform designed for writing, reading, and interacting with blogs. With Bloxy, users can easily share their thoughts, read engaging content, and comment on various topics. 

## Features

- **Create and Publish Blogs**: Users can write blogs with a rich text editor, format content, and publish them for everyone to see.
- **Read Blogs**: Explore various topics, authors, and categories through a streamlined reading interface.
- **Comment and Engage**: Engage with authors by leaving comments, starting discussions, and providing feedback.
- **User Profiles**: Each user has a profile with their blogs, bio, and more, making it easy to follow favorite authors.
- **Responsive Design**: Fully optimized for both desktop and mobile devices.

## Live Preview

Try out Bloxy live by visiting: [Bloxy Live Preview](http://ec2-3-93-215-26.compute-1.amazonaws.com/bloxy/dashboard)

> **Note:** This link points to the live version of Bloxy. Feel free to create, read, and comment on blogs to experience the platform in action.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (additional frameworks if used)
- **Backend**: Python3, Aquilify, Transutil
- **Database**: ElectrusDB
  
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/axiomchronicles/bloxy.git
    ```

2. Navigate to the project directory:
    ```bash
    cd bloxy
    ```

3. Setup Python Environment:
    ```bash
    python3 -m venv env
    ```

4. Install Dependencies
   ```
   pip install aquilify[full], electrus, netix, uvicorn, tansutil
   ```

5. Run the development server:
    ```bash
    aquilify runserver
    ```

6. Open the app in your browser at `http://localhost:29518`.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements or fixes.

1. Fork the project
2. Create a new branch for your feature: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add Your Feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Blogging on Bloxy!
