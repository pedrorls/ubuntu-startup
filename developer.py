developer = {
    "Inkscape":
        "sudo add-apt-repository ppa:inkscape.dev/stable -y" +
        " && sudo apt-get update && sudo apt-get install inkscape -y",
    "Sublime Text":
        "sudo add-apt-repository ppa:webupd8team/sublime-text-3 -y" +
        " && sudo apt-get update && " +
        "sudo apt-get install sublime-text-installer",
    "Atom":
        "sudo add-apt-repository ppa:webupd8team/atom -y" +
        " && sudo apt-get update && sudo apt-get install atom -y",
    "JDK":
        "sudo apt-get install default-jdk",
    "Docker":
        """sudo apt-get update && sudo apt-key
         adv --keyserver hkp://p80.pool.sks-keyservers.net:80
          --recv-keys 58118E89F3A912897C070ADBF76221572C52609D &&
         sudo apt-add-repository
         'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
         && sudo apt-get update sudo apt-get install -y docker-engine""",
    "Ruby2.4.0":
        """sudo apt-get update && sudo apt-get install
        git-core curl zlib1g-dev build-essential libssl-dev
        libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev
        libxslt1-dev libcurl4-openssl-dev python-software-properties
        libffi-dev nodejs
        cd
        git clone https://github.com/rbenv/rbenv.git ~/.rbenv
        echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
        echo 'eval "$(rbenv init -)"' >> ~/.bashrc
        exec $SHELL
        git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
        echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
        exec $SHELL
        rbenv install 2.4.0 && rbenv global 2.4.0 && ruby -v
        """,
    "Selenium":
        "pip install pyvirtualdisplay selenium",

}
