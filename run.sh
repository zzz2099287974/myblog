#!/bin/bash

# 检查命令行参数
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 {serve|deploy}"
    exit 1
fi

COMMAND=$1


case $COMMAND in
    serve)
        echo "Starting Hexo server..."
        hexo clean
        hexo generate
        hexo server
        ;;
    deploy)
        echo "Deploying Hexo site..."
        hexo clean
        hexo generate
        hexo deploy
        ;;
    *)
        echo "Invalid command. Use 'serve' to run the server or 'deploy' to publish the site."
        exit 1
        ;;
esac
