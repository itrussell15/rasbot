#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/ubuntu/rasbot/src/common_msgs/sensor_msgs"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/ubuntu/rasbot/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ubuntu/rasbot/install/lib/python3/dist-packages:/home/ubuntu/rasbot/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ubuntu/rasbot/build" \
    "/usr/bin/python3" \
    "/home/ubuntu/rasbot/src/common_msgs/sensor_msgs/setup.py" \
    egg_info --egg-base /home/ubuntu/rasbot/build/common_msgs/sensor_msgs \
    build --build-base "/home/ubuntu/rasbot/build/common_msgs/sensor_msgs" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/ubuntu/rasbot/install" --install-scripts="/home/ubuntu/rasbot/install/bin"
