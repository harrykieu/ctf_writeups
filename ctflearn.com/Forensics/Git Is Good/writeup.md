# Git Is Good
Extract and open the zip file, we found a folder name `gitIsGood`. Inside this folder has a `.git` folder, so this must be a git repository.  
The file `flag.txt` has a redacted (edited) flag, so we must find the previous flag. Open COMMIT_EDITMSG file, we can see that the file `flag.txt` was modified. Using Google, I found the command to check the list of commits and their hashes: `git log`  

![Screenshot 2022-09-19 163802](https://user-images.githubusercontent.com/89294020/190991288-42fab04c-5645-4973-a9e1-17fe0e0f7a82.png)

There are 2 commits, the one with `(HEAD)` is the current commit. To check the remaining commit, I use the command: `git checkout hash_of_commit` with the hashes `6e824...` and find the flag on the `flag.txt` file: `flag{protect_your_git}`
