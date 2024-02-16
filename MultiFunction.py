class MultipleFunctions():
        def Subfields():
            AI=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
            print("Sub-fields in AI are:")
            for SubfieldsAI in AI:
                print(SubfieldsAI)

        def OddEven():
            Number=int(input("Enter a number:"))
            if(Number%2==0):
                print(Number,"is Even number")
                message="Number is Even number"
            else:
                print(Number,"is odd number")
                message="Number is odd number"
                return message
        
        def Elegible():
            Gender=input("Your Gender:")
            Age=int(input("YourAge:"))
            if(Gender=="Male","m"):
                if(Age>=21):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")
            elif(Gender=="Female","f"):
                if(Age>=18):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")
                    
        def Percentage():
            Subject1=int(input("Subject1="))
            Subject2=int(input("Subject2="))
            Subject3=int(input("Subject3="))
            Subject4=int(input("Subject4="))
            Subject5=int(input("Subject5="))
            Total=Subject1+Subject2+Subject3+Subject4+Subject5
            print("Total:",Total)
            Percentage=((Total/500)*100)
            print("Percentage:",Percentage)
            
        def triangle():
            Height=int(input("Height:"))
            Breadth=int(input("Breadth:"))
            print("Area formula:(Height*Breadth)/2")
            Area=(Height*Breadth)/2
            print("Area of Triangle:",Area)
            Height1=int(input("Height1:"))
            Height2=int(input("Height2:"))
            Breadth=int(input("Breadth:"))
            print("Perimeter formula:Height1+Height2+Breadth")
            Perimeter=(Height1+Height2+Breadth)
            print("Perimeter of Triangle:",Perimeter)