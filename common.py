common = {
    "Google Chrome": "sudo sh -c 'echo 'deb [arch=amd64]" +
    " http://dl.google.com/linux/chrome/deb/ stable main' >>" +
    " /etc/apt/sources.list.d/google.list' && wget -q -O - " +
    "https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -" +
    " && sudo apt-get update && sudo apt-get install google-chrome-stable",

    "Spotify": "sudo sh -c 'echo" +
    " 'deb http://repository.spotify.com stable non-free' >> " +
    "/etc/apt/sources.list.d/spotify.list'' && sudo apt-key adv " +
    "--keyserver hkp://keyserver.ubuntu.com:80 --recv-keys D2C19886" +
    "sudo apt-get update && sudo apt-get install spotify-client -y",

    "VLC": "sudo add-apt-repository ppa:videolan/stable-daily -y &&" +
    " sudo apt-get update && sudo apt-get install vlc -y",
    "Pomodoro Gnome": "sudo apt-get install gnome-shell-pomodoro",
}
