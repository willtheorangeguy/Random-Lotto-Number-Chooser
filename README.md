# Random Lotto Number Chooser

[![Join the chat at https://gitter.im/willtheorangeguy/Random-Lotto-Number-Chooser](https://badges.gitter.im/willtheorangeguy/Random-Lotto-Number-Chooser.svg)](https://gitter.im/willtheorangeguy/Random-Lotto-Number-Chooser?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


This random lotto nuumber chooser will automatically pick 6 random numbers for you. 

Thanks to Mike McGrath for the idea.


## Insalation and Operation

### Through the Python Module (IDLE)
-	Download the Python module if you haven’t already: [Download Link](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe), and install it,
-	Extract files from your GitHub Download,
-	Double click the lotto.py file in File Explorer,
-	And the app will open for you to use!

### Creating a Executable File Through cx_Freeze (Windows Only)
-	Download cx_Freeze if you haven’t already: [Download Link](https://pypi.python.org/packages/b7/64/2e8bbd862e72253d0aee6e69a30e06af1baa11bcc96c1ffb2a4303fb6b23/cx_Freeze-4.3.4.win32-py3.4.exe#md5=bd087416c69ced533768a22e5d3414b8), and install it,
-	Extract the files from your GitHub download to this location on your computer: C:\Users\YOUR_USERNAME,
-	Open Command Prompt and type the following command:
```
python setup.py bdist_msi
```
-	Run the .msi file that the process creates in a dist sub-directory to create an executable,
-	Run the executable and the app will open for you to use!

## Use Instructions
- Click the 'Get My Lucky Numbers' button in the bottom left hand corner of the app.

![Screenshot](https://raw.githubusercontent.com/willtheorangeguy/Random-Lotto-Number-Chooser/master/Screenshot2.PNG)

- The app will then generate 6 random numbers to replace the '...' in the top 6 squares. 

![Screenshot](https://raw.githubusercontent.com/willtheorangeguy/Random-Lotto-Number-Chooser/master/Screenshot.PNG)

- Cick the reset button in the bottom right corer to get new numbers.

## Releases
The current release is 1.6. The next release, either 1.7 or 2.0 will hopefully becomming out soon with the following features:
- Number amount control
- Number limit

Your Pull Requests for new features are always welcome! Look to see some of your suggestions in upcomming updates.


## Bugs and Issues
Who likes bugs? If you’ve found any feel free to let me know on the issues page and I will make sure to fix them in short order, and release those fixes in new releases. 

**Note:** Please check the known issues list below before posting an issue to see if your issue us already on the list.
- No current know issues


## Maintainer
@willtheorangeguy


## A Quick Note
The reason why (if you where wondering) none of the pull requests go through Travis CI or Circle CI before getting merged is because, first, I haven’t really figured it out yet (I’d love some help), second, the project is so small I don’t really need it (but I’d like it), third, I like testing out the builds myself, so it fits really well. An that’s why!
