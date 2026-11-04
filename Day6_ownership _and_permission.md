#Ownership and permission

=> we can change the ownership of a user or group

=> there are 3 types of permission

- Read(r)-4-
- write(w)-2-
- Excute(x)-1-

=> there still the permission have 3 parts
user -group -other

drwx r-x r-x

--CHMOD method--
=> chmod <parameter> filename

Special file permissions
=> SUID bits(s)- set user ID bit - add 4 infront of our numeric value -> 4000
=> SGID bits(s)- set group ID bit - add 2 infront of our numeric value -> 2777
=> sticky bits(t)- set other ID bit - add 1 infront of our numeric value -> 1602
