developer = {
    "Inkscape":
        "sudo add-apt-repository ppa:inkscape.dev/stable -y" +
        " && sudo apt-get update && sudo apt-get install inkscape -y",
    "Sublime Text":
        "sudo add-apt-repository ppa:webupd8team/sublime-text-3 -y" +
        " && sudo apt-get update && " +
        "sudo apt-get install sublime-text-installer -y",
    "Atom":
        "sudo add-apt-repository ppa:webupd8team/atom -y" +
        " && sudo apt-get update && sudo apt-get install atom -y",
    "JDK":
        "sudo apt-get install default-jdk -y",
    "Docker":
        "sudo apt-get update && sudo apt-key" +
        " adv --keyserver hkp://p80.pool.sks-keyservers.net:80" +
        " --recv-keys 58118E89F3A912897C070ADBF76221572C52609D &&" +
        " sudo apt-add-repository" +
        " 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'" +
        " && sudo apt-get update sudo apt-get install -y docker-engine",
    "Ruby2.4.0":
        "sudo apt-get install libgdbm-dev libncurses5-dev automake libtool" +
        " bison libffi-dev" +
        " && gpg --keyserver hkp://keys.gnupg.net --recv-keys" +
        " 409B6B1796C275462A1703113804BB82D39DC0E3" +
        " && curl -sSL https://get.rvm.io | bash -s stable" +
        " && source ~/.rvm/scripts/rvm" +
        " && rvm install 2.4.0 && rvm use 2.4.0 --default && ruby -v &&" +
        " gem install bundler",
    "Selenium":
        "pip install pyvirtualdisplay selenium",
    "Gimp":
        "sudo add-apt-repository ppa:otto-kesselgulasch/gimp -y" +
        " && sudo apt-get update && sudo apt-get install gimp -y",
    "Android IDE":
        "sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make -y &&" +
        " sudo apt-get update && sudo apt-get install ubuntu-make -y &&" +
        " sudo umake android android-ndk && sudo umake android android-studio",

}
