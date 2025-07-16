name = input("Enter the server jar name (e.g. server.jar): ")
minram = input("Enter the amount of minRAM to allocate (e.g. 1024M): ")
maxram = input("Enter the amount of maxRAM to allocate (e.g. 2048M): ")
command = f"java -Xmx{maxram} -Xms{minram} -jar {name} nogui"
print(command)
input("Press Enter to exit...")
exit(0)