#Linux user managment

-> every root id is 0

- Root id = 0
- Root user can do every thing and can get in everywhere

-> Normal user id starts with 1-999

sudo lets normal user to access what a root can

sudo => super user do

--->Create user

=> on linux to create user u can use the ff commands:

- Useradd: eg. (sudo useradd meti)

- Adduser: eg. (sudo Adduser meti)

-> etc/shadow => contain the user password but it is encrypted

- cat/etc/shadow

-> id -tells the id of the user

-> sudo su :- to enter a root

->whoami :- tells where u are

---

#Further on linux user managment

-> To update/change password:

eg. sudo passwd meti

-> To change user and group id:

eg. - sudo usermod -u (new user id) username -> for user

    - sudo groupmod -g (new user id) groupname -> for group

-> To delete user:
-sudo userdel -r username

-> To login to the created user:
-sudo - username

-> To create personal file on home directory for user:

- sudo mkhomedir_helper username

-> To change shell for user:

- sudo usermod username -s /bin/bash

-> To add user to a group:

- sudo usermod -aG groupname username

-> To remove a user from a group:

- sudo gpasswd -d username groupname or
- sudo deluser username groupname

-> To add a user to sudoers:
to open sudoers => sudo visudo
then add the user to the previlages
