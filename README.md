[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Bp585G7b)

The program is written in python programming language. Thus, make sure that you have installed all the nessesary configuration files.

Setting up the environment:

1. Check if you have python installed.
Enter the terminal window and type python --version(this command is suitable for any OS). If the version is displayed, then you are ready to go to the next step!
If the command is not found, you have to download python by going to python.org. Choose the setup file according to your OS. After installation process check the python --version command in the terminal. Now, if everything is installed properly, you should see the installed version of python.

2. Check if you have git installed(git --version), because you will use git clone command to clone the repository too your local system. 
If the command is not found follow the same procedure- go to the official git-scm.com and download according to your OS.

Now, let's go to next step:

1. Create a new folder on Desktop called distributed_systems. 
2. Go to the github link https://github.com/ADA-GWU/understanding-the-systems-with-complex-connections-NarminaKarimova. There you will see the green code button.
3. Copy the link and retrun to the terminal window.
4. Go to the path of new created folder(cd Desktop/distributed_systems)
5. write git clone https://github.com/ADA-GWU/understanding-the-systems-with-complex-connections-NarminaKarimova.git
6. Now you have all the source codes of the program.
7. cd understanding-the-systems-with-complex-connections-NarminaKarimova

Running the application:

1. Open 3 more terminal windows and repeat the steps 4 and 7, so you will be in the path where you will run your client and server applications.
2. in first 3 windows write python server.py <port> 
P.S instead of <port> specify the port that is available on your system.
Example: in the first window write "python server.py 9001"
         in the second window write "python server.py 9002"
         in the third window write "python server.py 9003"

Thus, you will start 3 server programs which will listen on the specified ports at the same time

If everything is done properly you will see something like this:
Server bound to port: 9001
Server is listening on port 9001

Server bound to port: 9002
Server is listening on port 9002

Server bound to port: 9003
Server is listening on port 9003

3. In the last window you should type python client.py <port1> <port2> <port3>

Example: client.py <9001> <9002> <9003>
P.S Here the numbers of ports should be the same as you specified in the 3 server applications.

If everything is correct, then you should see the following:

Enter a number (connected to port 9001, 'exit' to quit):

4. Now you should enter any number and the result will appear in the window where your server is running on the port 9001, so if you input , you will see 10 in the according server window.
5. Type exit to switch to 9002 port and repeat the same.
6. Thus, you will subsequently connect to server applications
7. When you reach the port 9003- last one, if you write exit, the client program will stop its execution. 


