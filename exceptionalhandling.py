# =============================================================================
# Exceptional Handling
# =============================================================================
try: ## main program here

except: ## run when error occurs
    
finally: ## always run whetehr error occurs or not


# =============================================================================
# Examples 
# =============================================================================

try:
    sum=10+"20"
except:
    print("you can't add int and string together")
    
finally:
    sum=10+20
    print(sum)
    

try:
    file=open("new_file","w")
    file.write("Hello world")
    file.close()
    file=open("new_file","r")
    #file.write("Hello World")
except FileNotFoundError:
    print("file not found")
except OSError:
    print("error")
else:
    print(file.read())
finally:
    file=open("new_file","w")    
    file.close()
