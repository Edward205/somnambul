# Somnambul
(som-nuhm-buhl)

 Display your sleep stage on Discord 
</p>

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

# What is this?
Somnambul integrates the Sleep as Android app with Discord through Tasker and a Django server. Sleep as Android sends sleep stage updates to Tasker, which sends GET requests to the Django server to update the Discord status using pypresence.

The current release from 04.02.2023 (v0.1) was created in an hour and a half, so it's very simple. Stay tuned for updates and developments.
# Requirements
Unfortunately I have used paid apps in order to create this. However, I am looking for alternatives, although I doubt I will find an alternative to Sleep as Android that offers good quality sleep tracking with lots of tracking devices and automation compatibility.
 * Sleep as Android - https://play.google.com/store/apps/details?id=com.urbandroid.sleep
 * A Sleep as Android compatible sleep tracker (I use Xiaomi Mi Band 6)
 * Tasker - https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm
 * Django - tested with Django 4.1.6
 * Pypresence - https://github.com/qwertyquerty/pypresence
 * Due to Pypresence, only Python versions 3.8 and above are supported
 
# Usage
Assuming you have Sleep as Android, Tasker and Django installed.
1. Enable Tasker automation in Sleep as Android
2. Install the Somnambul Tasker project **PLEASE CHECK BACK SOON**
3. Change the IP address of the vars to that of the machine you will be hosting Discord and Django on.
4. Download the code for this project
5. Open a terminal into the directory of the project and type `python manage.py runserver`
6. Make sure the Discord client is open on the machine running the Django server.
7. Use the test task in Tasker to see if it works
8. If your status in Discord is "Playing a game: Waiting for sleep tracking", you are ready to go to sleep and your sleep stage status will be updated

# License
This project is [licensed under the MIT licence.](https://github.com/Edward205/somnambul/blob/main/LICENSE)

# To-do
* Add more details to this document
* Add multiple langauages
* More information about sleep in status
* Add icons
* Find an alternative to Tasker
* Remake HTTP server in C++
