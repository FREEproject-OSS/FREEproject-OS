echo "Enter your GitHub e-mail."
read email
echo "Enter your GitHub username."
read name

sudo git config user.email $email
sudo git config user.name $name

echo "You are now ready to commit and push. You will be prompted to login on push."
