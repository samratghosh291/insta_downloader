import instaloader

#create an instace of Instaholder class
l = instaloader.Instaloader()


#get a profile name from user input

profile = input("Enter the profile name: ")

#download the metadata and profile picture
l.download_profile(profile, profile_pic_only=True)
