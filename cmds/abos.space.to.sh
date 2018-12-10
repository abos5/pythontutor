#! /usr/local/bin/zsh

IN=$1
U=$2
port=26211

if [ ! $IN ]; then
    echo "Where do U wanna go ?"
    echo "d or s ?"
    read IN
fi

# default user
if [ $IN = 'q' ]; then
    DU="www"
    H="qq.abos.space"
elif [ $IN = 's' ]; then
    DU="www"
    H="ssh.abos.space"
elif [ $IN = 'd' ]; then
    DU="www"
    H="docker.abos.space"
elif [ $IN = 'aws' ]; then
    DU="www"
    H="aws.host"
    port=22
else
    echo "no space to go"
    exit 2;
fi

# if no user input
if [ ! $U ]; then
    U=$DU
fi

echo "connecting to ${U}@${H} ..."
ssh -p ${port} ${U}@${H} -v


