#!/bin/bash

echo -e "\n-------------------- Building library --------------------"
cd ../gambezi_dashboard_java
./build.sh
cd ../gambezi_test

echo -e "\n-------------------- Copying library --------------------"
if [[ ! -d build ]]; then
    mkdir build
fi
cp ../gambezi_dashboard_java/build/java_websocket.jar build/
cp ../gambezi_dashboard_java/build/gambezi.jar build/
cp ../gambezi_dashboard_java/build/gambezi_dashboard.jar build/

echo -e "\n-------------------- Compiling test --------------------"
javac -cp build/java_websocket.jar:build/gambezi.jar:build/gambezi_dashboard.jar -Xlint:unchecked -d build/ Main.java

echo -e "\n-------------------- Running test --------------------"
java -cp build/java_websocket.jar:build/gambezi.jar:build/gambezi_dashboard.jar:build Main
