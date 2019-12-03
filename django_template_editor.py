import re
with open('z.txt', 'r+') as file:
                for line in file:
                    #print(line)
                    result = re.search('src="(.*?)"', line)
                    result2 = re.search('href="(.*?)"', line)
                    

                    if result :
                        try:
                            z = (result.group(1))
                            new_z = " {%static '"+z+"' %}"
                            
                            replace = line.replace(z, new_z)
                            print(replace)
                            #print(result)
                            #print(z)
                            
                            

                        except AttributeError:
                            z = (result)
                            #print(z)
                            #print(line.replace(z, " 'zayanto' "))



                    elif result2 :
                        try:
                            z2 = (result2.group(1))
                            new_z2 = " {%static '"+z2+"' %}"
                            
                            replace2 = line.replace(z2, new_z2)
                            print(replace2)
                            #print(result)
                            #print(z)
                            
                            

                        except AttributeError:
                            z = (result)
                        #print(z)


                    

                    else:
                        #file.write(line)
                        print(line)
                        #pass
                        

                  
