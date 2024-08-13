# Group Chat Django

This repository contains a Django project that implements a real-time group chat application using WebSockets with Django Channels. Users can create or join chat rooms and send messages in real-time.

## Features

- **Real-time Communication**: Users can send and receive messages instantly using WebSockets.
- **Multiple Chat Rooms**: Users can create or join different chat rooms.
- **Scalable Architecture**: Built with Django Channels for handling WebSocket connections.

## Requirements

- Python 3.x
- Django
- Django Channels
- Redis (for channel layers)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/group-chat-django.git
   cd group-chat-django

2. Run redis:
   ``` bash
   redis-server

## Project Structure
1. views.py: Contains views for creating chat rooms and rendering the chat room page.
2. consumers.py: Defines the WebSocket consumer that handles real-time communication between clients in a chat room.
3. models.py: Contains the Room model representing a chat room.
4. urls.py: Maps the URLs to the corresponding views.
5. routing.py: Defines the routing for WebSocket connections.
6. templates/: Contains HTML templates for the chat interface.
7. 
# WebSocket Communication
The real-time chat functionality is implemented using Django Channels and WebSockets. Below is an overview of how WebSocket communication is handled:

Connection: When a user connects to a chat room, a WebSocket connection is established, and the user is added to a group corresponding to that room.

# Message Handling:

- receive: When a message is received from a client, it is broadcasted to all clients in the same group (chat room).
- chat_message: This method handles sending the message to the WebSocket, which is then displayed to all connected users.
- Disconnection: When a user disconnects, they are removed from the group.

Running the Application
Create or Join a Chat Room:

Go to the home page and enter a room name to create or join a chat room.
Send Messages:

Once in a room, users can send messages in real-time that will be visible to all participants in the room.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue if you have any suggestions or find any bugs.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
