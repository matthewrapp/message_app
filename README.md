# Overview

This software demonstates the use of sockets within a chat application. The demonstation and software isn't very complex, but to have barebones socket app working effeciently, is something I wanted to do and learn more about. Everything is through the commandline, including the chat interface.

[Software Demo Video](https://youtu.be/Y6OmXW5QMIo)

# Network Communication

In this software I have a client.py file that starts up the client and have a server.py file that starts up the server. I am using TCP sockets, which requires an established connection to trasmit data.

For the server I have using `0.0.0.0` for the host and `5002` for the port.
<br><br/>
For the client, I am using `localhost` or `127.0.0.1` for the host and `5002` for the port.

# Development Environment

Tools used to develop this program:

* VS Code
* Command Line/Terminal

Programming languages and libraries used to develop this program:

* Python3
* Thread
* socket
* random
* datetime
* colorama

# Useful Websites

* [GeeksforGeeks](https://www.geeksforgeeks.org/)
* [Stack Overflow](http://stackoverflow.com)

# Future Work

* Add an interface to this application. Something elegant and easy to use.
* Push this to production somewhere where I can test it across IP Addresses