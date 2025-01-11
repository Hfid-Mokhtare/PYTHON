#-----------------------------------
#-- Exceptions Handling ------------
#-- Try | Except | Else | Finally
#--     Advanced Example   ---------
#-----------------------------------

the_file=None
tries=5

while tries>=0:

    try:
        print(f"you have only {tries} tries left : ")
        the_file_pathe= input ("please enter the file pathe : ").strip()
        the_file=open(the_file_pathe,"r")
        print(the_file.read())
        break
    except FileNotFoundError:
        print ("the file is not found")
        tries-=1
    except Exception as e:
        print(f"there is an error :( {e}")
        tries-=1
    finally:
        if the_file is not None:
            the_file.close()
            print("the operation is done and the file was closed")
else :
    print("All Tries is Done")
        
       
