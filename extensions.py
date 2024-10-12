# function that checks user media type
def media_type_check(media):
    match media:
        # case _ is a wildcard, which mean "match anything.
        # the if part adds a condition to check whether that pattern meets a specific requirement
        # endswith() checks whether a string ends with a specified suffix
        case _ if media.endswith(".gif"):
            print("image/gif")
        case _ if media.endswith(".jpg"):
            print("image/jpeg")
        case _ if media.endswith(".jpeg"):
            print("image/jpeg")
        case _ if media.endswith(".png"):
            print("image/png")
        case _ if media.endswith(".pdf"):
            print("application/pdf")
        case _ if media.endswith(".txt"):
            print("text/plain")
        case _ if media.endswith(".zip"):
            print("application/zip")
        case _:
            print("application/octet-stream")

#main function
def main():
    media_type = input("File name: ").lower().strip()
    media_type_check(media_type)

main()
