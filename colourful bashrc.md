It is common to have a rather useless Bash prompt. in order to turn it into a colourful useful one, (e.g.: `[14:33] username@machine:~/currentdir$`), paste this in your home directory in a file named `.bashrc`

    # .bashrc

    # Source global definitions
    if [ -f /etc/bashrc ]; then
            . /etc/bashrc
    fi

    # User specific aliases and functions

    # Cluster
    export CLUSTER=`ls /mapr`

    # Setup Development environtment
    source /mapr/${CLUSTER}/projects/resbi/software/env.sh
    source /mapr/${CLUSTER}/projects/resbi/data/alias

    # Colors of bash
    eval `dircolors`
    export LS_COLORS="di=00;36:fi=37:ex=00;32"
    export PS1=$'\[\e[0;32m\][\A]\[\e[0;31m\] \u@\h:\[\e[0;36m\]\w$\[\e[0;37m\] ';

In order to see the canges immediately, just run `source ~/.bashrc`.
