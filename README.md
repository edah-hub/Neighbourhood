# Neighbourhood
[![Screenshot-from-2022-06-19-23-31-09.png](https://i.postimg.cc/6pt0TFzB/Screenshot-from-2022-06-19-23-31-09.png)](https://postimg.cc/YhDgsnJP)

## Description
This is a web application allows you to be in the loop about everything happening in your neighborhood. From contact information of different neighbours to meeting announcements or even alerts.

## Technologies Used
- python-3.9
- Django
- Postgresql
- MDBootstrap

##### Requirements
- python-3.9/pip
- Django
- Code/text editor
- Virtual environment (virtualenv)

##### Setup Instructions and Installation

- Clone this repository to a location in your file system. `git clone https://github.com/edah-hub/Neighbourhood.git`
- Open terminal command line then navigate to the root folder of the application. `neighbourhood`
- Open with `python3 manage.py runserver` on your Browser.

## Behaviour Driven Development

| Behavior                | Input description  | Output description                                    |
| ----------------------- | ------------------ | ----------------------------------------------------- |
| Login, Signup or Logout | Username, Password | User will be either loggedin, registered, loggedout   |
| upload a business       | name, description, image  | The business will be posted to the Neighbourhood page |

## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request