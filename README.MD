# Simple todolist made by Django

## Example
![img.png](readmeAssets%2Fimg.png)

You can add items by typing in the input field and pressing the `Add` button.\
You can also delete items by pressing the `Delete` button.
- This program only supports one user.
- The data isn't saved after the server is closed.
- So every time you enter the site, the data is reset.


## Branch info
- master: The main branch
- develop/todos: The branch for the main development of the project
    - Implemented CRUD
    - Implemented Test case, but failed. (I'm fixing it)
    - Adopted session to store data of user, but failed. (I'm fixing it)
- develop/todos-advanced: The branch for the advanced development of the project
    - Adopted session to store data of user
    - Implemented AJAX to update the page without refreshing, but failed (I'm fixing it).
![branch.png](readmeAssets%2Fbranch.png)

## Further development
1. Adopt WebSocket to manage multiple users.
2. Solve concurrency issues.