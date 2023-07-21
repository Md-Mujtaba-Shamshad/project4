import instaloader

ing = instaloader.Instaloader()

profile = input("Enter profile Name: ");
username = input("Uesrname: ")

ing.download_profile(profile,profile_pic_only=True)
print("Download successfull")


