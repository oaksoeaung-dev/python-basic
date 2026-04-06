number = input("Enter number: ")

# try:
#     result = int(number) / 2
#     print(result)
#     print("Process successful.")

#     #file = open("input.txt","w") #overwrite
#     # file = open("input.txt","a") #append #persistance storage
#     # file.write(str(result) + "\n")
#     # file.close()
#     with open("input.txt","a") as file:
#         file.write(f"{result}\n")
# except Exception as ex:
#     print("Error happened! ",ex)
# finally:
#     print("All Done!")
#     with open("input.txt","r") as file: #read
#         file_result = file.read()
#         print(file_result)

with open("input.txt","a+") as file:
    try:
        result = int(number) / 2
        file.write(f"{result}\n")
    except Exception as ex:
        print("Someting went wrong!.",ex)
    finally:
        print("All done!")
        file.seek(0)
        file_result = file.read()
        print(file_result)
    

