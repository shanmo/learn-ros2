## about 

- learning notes from https://fishros.com/d2lros2/#/

## setup  

- tried galactic from robostack https://robostack.github.io/ 
    - after building the package, cannot find .bash files after sourcing install/setup.bash 
    - need to copy all the files in install to the workspace folder, but still cannot launch the package 

- use docker 
    - https://github.com/athackst/dockerfiles
    - blog https://www.allisonthackston.com/articles/docker-development.html
    - this also failed due to not having nvidia gpu 

- use docker with vnc 
    - https://github.com/Tiryoh/docker-ros2-desktop-vnc
    - use safari to enter `http://127.0.0.1:6080/`
    - need to solve permission issue https://www.cnblogs.com/feifanrensheng/p/15972259.html
        - `sudo chmod 777 -R ~/.ros/`